# NewPipe 1.3.5 — OAuth Google próprio para subscrições

## O que mudou nesta versão

A versão 1.3.5 usa estritamente o fluxo oficial **OAuth 2.0 para dispositivos com entrada limitada** da Google:

1. O NewPipe solicita um `device_code` com o Client ID configurado nas definições.
2. A Google devolve `verification_url` e `user_code`.
3. O QR abre **exatamente** o `verification_url` devolvido: normalmente `https://www.google.com/device`.
4. No navegador, informe o **Código de ativação** que o submenu mostra.

> O QR pode parecer igual em todos os logins porque ele abre a mesma página oficial Google. Isto está correto: o elemento temporário e associado ao projeto é o **Código de ativação**, que muda a cada pedido.

A rota `youtube.com/qr/activate/<código>` foi removida. Ela pertence ao fluxo interno do YouTube TV e estava a encaminhar a autorização para a identidade `kodi11`, em vez de usar o Client ID OAuth configurado no NewPipe.

## Instalação

1. Instale `plugin.video.newpipe-1.3.5-oauth-google-oficial.zip` por cima da versão anterior.
2. Abra **Configurações → Conta do YouTube**.
3. Confira o **ID do cliente OAuth Google (TV)** e o segredo do seu projeto atual.
4. Selecione **Fazer login no YouTube**.
5. Abra **Abrir QR Code (página Google)** em outro ecrã/dispositivo, ou abra manualmente `https://www.google.com/device`.
6. Digite o **Código de ativação** mostrado abaixo do QR.
7. Autorize e volte ao submenu para selecionar **Verificar ligação agora**.

## Sem fallback de projeto

O NewPipe 1.3.5 não usa Client IDs alternativos e não reutiliza o fluxo do SmartTube. Se o Client ID configurado for inválido, o add-on apresenta um erro — não muda para outro projeto.

Referência oficial: [OAuth 2.0 para TVs e dispositivos de entrada limitada](https://developers.google.com/identity/protocols/oauth2/limited-input-device).
