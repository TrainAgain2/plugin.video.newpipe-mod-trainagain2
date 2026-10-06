# NewPipe MOD 1.4.12 — instalação autónoma

Esta MOD é **autónoma**: instale somente o ZIP `plugin.video.newpipe-1.4.12-mod.zip`.

> Não instale repositório Kodi adicional nem módulos externos como Tulip, URL Dispatcher, Scrapetube, Unicache, ResolveURL, PluginsGR e Kodi Six. As bibliotecas necessárias já acompanham o próprio ZIP da MOD.

## Instalação

1. No Kodi, abra **Add-ons → Instalar a partir de ficheiro ZIP**.
2. Escolha `plugin.video.newpipe-1.4.12-mod.zip`.
3. Aguarde a notificação **Add-on instalado**.
4. Abra **Vídeos → Add-ons de vídeo → NewPipe MOD**.

## O que está incluído

| Componente | Utilização no NewPipe MOD |
|---|---|
| Tulip | Criação de listas e comunicação com a interface Kodi |
| URL Dispatcher | Navegação das rotas internas |
| Scrapetube e requests | Pesquisa, canais, playlists e paginação YouTube |
| Unicache | Cache de consultas |
| Kodi Six | Camada de compatibilidade Kodi do motor de streams |
| Motor YouTube nativo | Obtenção do stream direto de áudio/vídeo |

A reprodução HLS usa o **InputStream Adaptive** quando esse componente já estiver disponível no Kodi; ele não é uma dependência externa de instalação desta MOD.

## Atualização

- Instale o ZIP 1.4.12 por cima de uma versão anterior do `plugin.video.newpipe`.
- As definições, histórico, favoritos, subscrições locais e sessão do YouTube são mantidos no perfil do add-on.
- Caso o Kodi mostre uma versão antiga do menu, use **Configurações → Limpar cache** e reinicie o add-on.

## Diagnóstico

Se o Kodi mostrar um erro durante a instalação, confirme que o ZIP contém a pasta raiz `plugin.video.newpipe/` e que o `addon.xml` declara somente `xbmc.python`, componente padrão do Kodi 20/21.
