# = NewPipe Kodi addon git repository =
## Privacy-first YouTube client for Kodi

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/D1D11UQ0IO)
[![Patreon](https://img.shields.io/badge/Patreon-support-orange)](https://www.patreon.com/c/twilight0)
[![PayPal](https://img.shields.io/badge/PayPal-donate-blue)](https://www.paypal.com/paypalme/AliveGR)

![](https://raw.githubusercontent.com/Twilight0/plugin.video.newpipe/master/icon.png)

NewPipe brings the [NewPipe Android app](https://newpipe.net/) philosophy to Kodi:
watch YouTube with **no account, no official API key, no tracking** — everything
personal stays in plain JSON files inside the addon profile on your own device.

## Why this exists

- The official YouTube addon needs API keys with quotas, and a Google account
  for subscriptions. Both tie viewing habits to an identity.
- Scraping-based clients prove you don't need either: listings come from public
  pages through the bundled Scrapetube library, while playback is resolved
  locally through the bundled mobile YouTube engine and sent directly to Kodi.
- Your subscriptions, playlist bookmarks, watch/search history never leave the
  box. Delete the profile files (or uninstall) and everything is gone —
  the same local-only guarantee NewPipe Android makes.

## Features

- Search videos / channels / playlists (with local search history)
- Trending and Live browsers (per-category, cached)
- Channels: videos, shorts, live streams, playlists
- Local subscriptions + subscription feed (per-channel item count setting)
- Playlist bookmarks (context menu on any playlist)
- Local watch history, audio-only mode, function-cache viewer + clear button
- "Go to channel" + Subscribe/Unsubscribe context menus on video items

## Known upstream limits (honest, not bugs here)

- YouTube removed the combined trending page server-side (`FEtrending` returns
  HTTP 400); Trending here is per-category view-count-sorted search, same
  tradeoff NewPipe Android itself documents.
- Playlist search was broken by a YouTube layout change (results moved to
  `lockupViewModel` nodes) — fixed in the bundled Scrapetube 2.8.1+ code.

## Requirements

- Kodi 20+ (Nexus/Omega). `inputstream.adaptive` is used only when a YouTube
  HLS manifest is selected by Kodi.
- No external `script.module.*` add-ons: Tulip, URL dispatcher, Scrapetube,
  Unicache, requests, Kodi Six and the YouTube resolver are included in the
  NewPipe ZIP.

**Primary OSes tested:**

- Garuda (Arch) Linux 64 bit

**Kodi versions tested:**

- Omega 21.x (x64)
