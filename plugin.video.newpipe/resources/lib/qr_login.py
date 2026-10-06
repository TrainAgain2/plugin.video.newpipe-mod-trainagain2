# -*- coding: utf-8 -*-
"""Kodi-native QR display for the Google device-verification link.

The QR is generated locally from Google's short-lived verification flow and displayed
inside NewPipe's own Kodi dialog.  It never opens SmartTube or another app.
"""
from __future__ import absolute_import

import hashlib
import os
import struct
import zlib

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import qrcode


_ACTION_CLOSE = (9, 10, 92, 216, 247, 257)
# ``WindowDialog`` controls use Kodi's fixed 720p logical canvas even when
# Android reports a physical 3120x1440 panel.  Coordinates based on either
# ``System.ScreenWidth`` or ``getScreenWidth`` therefore land off-screen.
_DIALOG_CANVAS_WIDTH = 1280
_DIALOG_CANVAS_HEIGHT = 720


def _screen_dimension(gui_method, label, fallback):
    """Use Kodi GUI coordinates, not the Android panel pixel resolution."""
    try:
        method = getattr(xbmcgui, gui_method, None)
        if method:
            value = int(method() or 0)
            if value > 0:
                return value
    except (AttributeError, TypeError, ValueError):
        pass
    try:
        value = int(xbmc.getInfoLabel(label) or 0)
        return value if value > 0 else fallback
    except (TypeError, ValueError):
        return fallback


def _profile_file(filename):
    profile = xbmcaddon.Addon('plugin.video.newpipe').getAddonInfo('profile')
    profile = xbmcvfs.translatePath(profile)
    if not xbmcvfs.exists(profile):
        xbmcvfs.mkdirs(profile)
    return os.path.join(profile, filename)


def _qr_file(qr_url):
    """Use a unique filename so Kodi cannot reuse an old QR thumbnail."""
    digest = hashlib.sha256(str(qr_url).encode('utf-8')).hexdigest()[:16]
    return _profile_file('newpipe-youtube-login-qr-{0}.png'.format(digest))


def _chunk(kind, payload):
    return (struct.pack('>I', len(payload)) + kind + payload +
            struct.pack('>I', zlib.crc32(kind + payload) & 0xffffffff))


def _write_gray_png(path, rows):
    """Write a small 8-bit grayscale PNG without Pillow or platform modules."""
    height = len(rows)
    width = len(rows[0]) if height else 0
    if not width or not height:
        raise ValueError('Cannot create an empty PNG')
    raw = b''.join(b'\x00' + bytes(row) for row in rows)
    data = (b'\x89PNG\r\n\x1a\n' +
            _chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 0, 0, 0, 0)) +
            _chunk(b'IDAT', zlib.compress(raw, 9)) + _chunk(b'IEND', b''))
    with open(path, 'wb') as handle:
        handle.write(data)


def _write_qr_png(value, path, module_size=10):
    encoder = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=1,
        border=4,
    )
    encoder.add_data(value)
    encoder.make(fit=True)
    matrix = encoder.get_matrix()
    rows = []
    for row in matrix:
        expanded = []
        for dark in row:
            expanded.extend(([0] if dark else [255]) * module_size)
        rows.extend([expanded] * module_size)
    _write_gray_png(path, rows)


def _write_panel_png(path):
    # A one-pixel dark image which Kodi stretches behind the controls.
    _write_gray_png(path, [[25]])


class _QRLoginWindow(xbmcgui.WindowDialog):
    """Screen-size-aware, closeable modal dialog built only with Kodi controls."""

    def __init__(self, qr_path, panel_path, code, activation_url):
        super(_QRLoginWindow, self).__init__()
        # Use the explicit WindowDialog coordinate canvas. Android's physical
        # resolution is only for rendering and is automatically scaled by Kodi.
        width = _DIALOG_CANVAS_WIDTH
        height = _DIALOG_CANVAS_HEIGHT
        # Keep the dialog deliberately compact inside the logical canvas.
        dialog_width = min(int(width * 0.72), 960)
        dialog_height = min(int(height * 0.60), 560)
        left = (width - dialog_width) // 2
        top = (height - dialog_height) // 2
        padding = max(24, int(dialog_height * 0.06))
        qr_size = min(280, int(dialog_height - 2 * padding), int(dialog_width * 0.35))
        qr_x = left + padding
        qr_y = top + (dialog_height - qr_size) // 2
        text_x = qr_x + qr_size + padding
        text_width = left + dialog_width - text_x - padding

        self._close = xbmcgui.ControlButton(
            left + dialog_width - 198, top + dialog_height - 62, 150, 40,
            'Fechar')
        controls = [
            xbmcgui.ControlImage(left, top, dialog_width, dialog_height, panel_path),
            xbmcgui.ControlImage(qr_x, qr_y, qr_size, qr_size, qr_path),
            xbmcgui.ControlLabel(text_x, top + padding, text_width, 55,
                                  'Fazer login no YouTube', font='font40'),
            xbmcgui.ControlLabel(text_x, top + padding + 62, text_width, 36,
                                  'Aponte a câmara para o QR Code', font='font30'),
            xbmcgui.ControlLabel(text_x, top + padding + 108, text_width, 36,
                                  'ou abra: ' + activation_url, font='font28'),
            xbmcgui.ControlLabel(text_x, top + padding + 165, text_width, 36,
                                  'Código de ativação:', font='font30'),
            xbmcgui.ControlLabel(text_x, top + padding + 206, text_width, 58,
                                  code, font='font50'),
            xbmcgui.ControlLabel(text_x, top + padding + 285, text_width, 50,
                                  'Depois de autorizar, o NewPipe sincroniza as subscrições automaticamente.',
                                  font='font26'),
            self._close,
        ]
        self.addControls(controls)
        self.setFocus(self._close)

    def onAction(self, action):
        if action.getId() in _ACTION_CLOSE:
            self.close()

    def onControl(self, control):
        if control == self._close:
            self.close()


def show(code, qr_url, activation_url='https://yt.be/activate'):
    """Create and show a QR modal inside NewPipe; return ``True`` on display."""
    if not code or not qr_url:
        raise ValueError('Activation code and QR URL are required')
    qr_path = _qr_file(qr_url)
    panel_path = _profile_file('newpipe-youtube-login-panel.png')
    _write_qr_png(qr_url, qr_path)
    _write_panel_png(panel_path)
    window = _QRLoginWindow(qr_path, panel_path, code, activation_url)
    try:
        window.doModal()
    finally:
        del window
    return True


def create(qr_url):
    """Create the QR image for Kodi's native picture viewer and return its path."""
    if not qr_url:
        raise ValueError('QR URL is required')
    qr_path = _qr_file(qr_url)
    _write_qr_png(qr_url, qr_path)
    return qr_path
