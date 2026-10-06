# NewPipe 1.2.0 — instalação sem dependências externas

Esta edição é **autónoma**: instale apenas o ZIP do NewPipe. Não instale Tulip, URL Dispatcher, Scrapetube, Unicache, ResolveURL, PluginsGR, Kodi Six nem qualquer repositório separado.

## Instalação

1. No Kodi, abra **Add-ons → Instalar a partir de ficheiro ZIP**.
2. Escolha `plugin.video.newpipe-1.2.0-autonomo.zip`.
3. Aguarde a notificação **Add-on instalado**.
4. Abra **Vídeos → Add-ons de vídeo → NewPipe**.

## O que está incluído

| Componente | Utilização no NewPipe |
|---|---|
| Tulip | Criação de listas e comunicação com a interface Kodi |
| URL Dispatcher | Navegação das rotas internas |
| Scrapetube e requests | Pesquisa, canais, playlists e paginação YouTube |
| Unicache | Cache de consultas |
| Kodi Six | Camada de compatibilidade Kodi do motor de streams |
| Resolver YouTube nativo | Obtenção do stream direto de áudio/vídeo |

A reprodução HLS usa o **InputStream Adaptive** quando esse componente já estiver disponível no Kodi; este não é uma dependência de instalação do add-on.

## Atualização da versão anterior

- O Kodi atualiza a versão 1.1.1 automaticamente porque esta edição usa a versão **1.2.0**.
- Pode deixar instalados os antigos módulos externos; eles deixam de ser usados pelo NewPipe.
- As definições, histórico, favoritos, subscrições locais e a sessão do YouTube existente são mantidos no perfil do add-on.

## Diagnóstico

Se o Kodi mostrar erro durante a instalação, confirme que selecionou o ZIP cujo nome termina em `autonomo.zip`. Este pacote contém a pasta raiz `plugin.video.newpipe/` e declara somente `xbmc.python`, que faz parte do Kodi 20/21.
