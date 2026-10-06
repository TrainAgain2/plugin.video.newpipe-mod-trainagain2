# Pesquisa técnica — autenticação SmartTube

## Evidência de implementação

A versão atual da árvore pública SmartTube utiliza a classe `com.liskovsoft.youtubeapi.auth.V2.AuthService` para o login YouTube. `YouTubeSignInService` e `YouTubeAccountManager` importam essa classe V2 diretamente e pedem um `user_code`, aguardando em seguida o `device_code` ser trocado por um `refresh_token`.

O pedido inicial do SmartTube é diferente do OAuth genérico que foi implementado no NewPipe:

- `POST https://www.youtube.com/o/oauth2/device/code`
- `Content-Type: application/json`
- Corpo JSON com `client_id`, `device_id`, `model_name: "ytlr::"` e um escopo YouTube TV.

A troca de código do SmartTube também usa o endpoint YouTube, JSON, e não o endpoint genérico `oauth2.googleapis.com/token`:

- `POST https://www.youtube.com/o/oauth2/token`
- Campos `code`, `client_id`, `client_secret` e `grant_type: "http://oauth.net/grant_type/device/1.0"`.

A interface do SmartTube gera dois endereços a partir do código: mostra `https://yt.be/activate` para entrada manual e põe no QR `https://youtube.com/qr/activate/<código>`. A classe da UI é `YTSignInPresenter`; ela acrescenta o código com os espaços convertidos em hífens.

O SmartTube não inclui permanentemente um Client ID/segredo no fluxo mostrado. A implementação consulta o JavaScript público do cliente YouTube TV, extrai os valores de cliente utilizados pelo próprio cliente TV e mantém uma cache. Isto está em `AppServiceCore`/`AppServiceCoreCached` e `ClientData`.

## Resultado dos ensaios sem autenticar uma conta

- O Client ID configurado no NewPipe aceitou os endpoints genérico Google e YouTube quando consultado apenas com `youtube.readonly`.
- O mesmo Client ID foi rejeitado pela chamada V2 exata do SmartTube quando foi solicitado o escopo `youtube-paid-content`: resposta `invalid_scope`.
- Portanto, não basta alterar o QR. Para reproduzir o SmartTube, o NewPipe precisa implementar o seu protocolo YouTube TV completo e obter os parâmetros do cliente TV compatível, em vez de usar o Client ID criado manualmente para o fluxo genérico.

## Consequência para o erro “kodi11”

A rota de QR do SmartTube só funciona corretamente quando está ligada a um código emitido pelo endpoint YouTube TV compatível. O NewPipe anterior criou o código noutro fluxo e depois colocou-o artificialmente na rota QR do YouTube TV. Essa mistura pode abrir uma identidade residual como `kodi11` e não pode ser corrigida trocando só o URL.

## Correção da importação após autorização

O log Kodi da ligação aprovada demonstrou que o token era guardado com sucesso, mas a primeira importação de canais falhava porque chamava `youtube.googleapis.com/youtube/v3/subscriptions`. A resposta indicava que a **YouTube Data API v3 não está habilitada no projeto do cliente público YouTube TV**. Portanto, esse erro era de catálogo, não de autenticação.

A versão 1.4.1 passa a consultar o feed autenticado interno do YouTube TV (`POST https://www.youtube.com/youtubei/v1/browse`, `browseId: FEsubscriptions`) com os cabeçalhos de cliente `TVHTML5` usados pelo SmartTube. Os renderizadores de canais desse feed são convertidos diretamente para as subscrições locais. A ação **Sincronizar subscrições do YouTube** continua disponível no menu quando a conta já está ligada, sem criar outro QR.

## Fontes

- Código público SmartTube: https://github.com/yuliskov/SmartTube
- `AuthApi` V2: https://github.com/yuliskov/SmartTube/blob/master/MediaServiceCore/youtubeapi/src/main/java/com/liskovsoft/youtubeapi/auth/V2/AuthApi.java
- `AuthApiHelper` V2: https://github.com/yuliskov/SmartTube/blob/master/MediaServiceCore/youtubeapi/src/main/java/com/liskovsoft/youtubeapi/auth/V2/AuthApiHelper.java
- UI de login YouTube: https://github.com/yuliskov/SmartTube/blob/master/common/src/main/java/com/liskovsoft/smartyoutubetv2/common/app/presenters/YTSignInPresenter.java
- Ajuda oficial para ativação de YouTube em TV: https://support.google.com/youtube/answer/3015415?hl=pt-BR
- OAuth Google genérico para dispositivos: https://developers.google.com/identity/protocols/oauth2/limited-input-device
