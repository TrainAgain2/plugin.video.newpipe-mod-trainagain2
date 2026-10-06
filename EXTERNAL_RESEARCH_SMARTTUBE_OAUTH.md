# Pesquisa: fluxo de login SmartTube e validação Google

**Data da verificação:** 2026-10-06

## Resultado

O aviso “A Google não validou esta app” é determinado no servidor Google pela **identidade do cliente OAuth** e pelo respetivo publicador. Não é removido por parâmetros de dispositivo como `model_name=ytlr::`.

A captura mostrou o publicador `firsthash@gmail.com`, pois a implementação inicial usou o par OAuth publicado em `constants.json` do SmartTube. Esse cliente não pertence ao NewPipe.

## O que o SmartTube faz

O código-fonte atual do SmartTube usa `auth.V2.AuthService` para login. A classe `AppServiceCore` obtém `clientId` e `clientSecret` ao descarregar e analisar o JavaScript do cliente Android TV do YouTube. O próprio comentário de `ClientData.java` descreve esses dados como o cliente de dispositivo Android TV.

> `ClientData.java`: “We need first occurrence … (Android TV device).”

O uso desses valores por um add-on independente faria o NewPipe apresentar-se como a aplicação oficial de TV do YouTube. Isso não é um mecanismo de validação que o add-on possa apropriadamente reproduzir.

## Verificação prática

A implementação do NewPipe já enviava `model_name: ytlr::`. Foi testado também o escopo V2 atual do SmartTube:

```text
http://gdata.youtube.com https://www.googleapis.com/auth/youtube-paid-content
```

Em 2026-10-06, o endpoint `https://www.youtube.com/o/oauth2/device/code` respondeu:

```text
HTTP 400
invalid_scope: Invalid device flow scope: https://www.googleapis.com/auth/youtube-paid-content
```

Portanto essa variante não foi empacotada.

## Caminho correto para remover o aviso

Para que a conta Google não exiba o aviso, o NewPipe precisaria de um **cliente OAuth próprio**, criado e verificado pelo respetivo proprietário no Google Cloud. A verificação é um processo do Google que envolve a configuração da tela de consentimento, domínio/política quando exigidos e análise da Google.

Como alternativa limitada, um cliente OAuth próprio em modo de testes pode autorizar apenas as contas adicionadas como utilizadoras de teste, mas o estado de verificação continuará a ser definido pelo Google.

## Fontes consultadas

- SmartTube source: https://github.com/yuliskov/SmartTube
- `youtubeapi/auth/V2/AuthApiHelper.java`
- `youtubeapi/service/YouTubeSignInService.java`
- `youtubeapi/app/AppServiceCore.java`
- `youtubeapi/app/models/ClientData.java`
- Google OAuth authentication guide: https://developers.google.com/youtube/v3/guides/authentication
