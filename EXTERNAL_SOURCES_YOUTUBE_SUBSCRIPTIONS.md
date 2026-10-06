# Referências externas — subscrições YouTube e OAuth próprio

## Implementação adotada: NewPipe 1.2.7

O NewPipe usa o fluxo oficial de autorização OAuth 2.0 para dispositivos de entrada limitada, com um cliente OAuth criado pelo próprio utilizador no Google Cloud.

- **Pedido de código:** `POST https://oauth2.googleapis.com/device/code`
- **Consulta/autorização/renovação de token:** `POST https://oauth2.googleapis.com/token`
- **Grant do dispositivo:** `urn:ietf:params:oauth:grant-type:device_code`
- **Escopo mínimo:** `https://www.googleapis.com/auth/youtube.readonly`
- **Importação:** `GET https://www.googleapis.com/youtube/v3/subscriptions?part=snippet&mine=true&maxResults=50`

O código exibe o `verification_url` e o `user_code` exatamente como a Google devolve. A imagem QR leva apenas ao URL de verificação; o utilizador informa o código na página da Google.

O guia geral de gestão de clientes OAuth descreve clientes nativos como públicos. Porém, a documentação específica do fluxo OAuth para TVs e dispositivos de entrada limitada exige `client_secret` no pedido ao endpoint de token. O teste real deste cliente Google confirmou a exigência com `Missing required parameter: client_secret`; por isso o NewPipe 1.2.9 exige o ID e o segredo do mesmo cliente antes de iniciar o fluxo.

## Por que o login SmartTube não é reutilizado

O SmartTube possui uma implementação distinta, mas o seu código extrai do JavaScript do YouTube a identidade do cliente OAuth de Android TV. Reutilizar essa identidade num add-on separado faria o NewPipe apresentar-se como a aplicação de outra parte. A validação no Google continua associada ao dono do cliente OAuth, não ao parâmetro de modelo enviado pelo dispositivo.

O endpoint atual também rejeitou, em 2026-10-06, o escopo V2 presente no SmartTube com `HTTP 400 invalid_scope`; por isso esse caminho não foi incluído.

## Fontes

1. Google, [OAuth 2.0 for TV and Limited-Input Device Applications](https://developers.google.com/identity/protocols/oauth2/limited-input-device) — endpoints, parâmetros, resposta e regras do fluxo de código de dispositivo.
2. Google, [YouTube Data API: subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list) — importação de subscrições autenticadas com `mine=true`.
3. Google, [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257) — classificação e gestão de clientes OAuth públicos/privados.
4. SmartTube, [código-fonte público](https://github.com/yuliskov/SmartTube) — comparação arquitetural de autenticação; não é usado para credenciais.
