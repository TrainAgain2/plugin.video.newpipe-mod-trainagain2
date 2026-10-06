# Referências externas — YouTube TV e subscrições

## Implementação adotada pelo NewPipe MOD

O NewPipe MOD utiliza o fluxo de ativação **YouTube TV** e a biblioteca autenticada do próprio YouTube. O código temporário é emitido pelo serviço YouTube TV, o QR abre a página oficial de ativação e os dados de conta ficam somente no perfil local do Kodi.

A sincronização de subscrições utiliza o endpoint autenticado `POST https://www.youtube.com/youtubei/v1/browse` com `browseId: FEsubscriptions`. Não utiliza a YouTube Data API v3 nem credenciais Google Cloud configuradas pelo utilizador.

## Fontes

1. YouTube, [iniciar sessão numa TV](https://support.google.com/youtube/answer/3015415?hl=pt-BR) — ativação de dispositivos com código.
2. Google, [OAuth 2.0 para TVs e dispositivos de entrada limitada](https://developers.google.com/identity/protocols/oauth2/limited-input-device) — contexto geral de códigos de dispositivo.
3. Google, [YouTube Data API: subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list) — referência da API v3, não utilizada pelo NewPipe MOD.
