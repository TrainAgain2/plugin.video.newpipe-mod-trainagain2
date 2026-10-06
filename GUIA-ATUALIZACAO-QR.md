# NewPipe 1.2.5 — correção do serviço e QR de login

## O que foi corrigido

O erro mostrado como **“NewPipe com erro”** após a instalação 1.2.0 era causado pelo serviço em segundo plano. No Android/Kodi, o serviço era iniciado a partir da pasta `resources/` e não conseguia carregar as bibliotecas internas do add-on.

A versão **1.2.5** adiciona os caminhos corretos do add-on e das bibliotecas internas ao serviço. Isto restaura a sincronização automática das subscrições depois do login no YouTube. O login não usa mais uma janela flutuante: ele abre um **submenu interno do NewPipe**. A resposta HTTP 428 do YouTube agora é corretamente entendida como “aguardando autorização”, portanto o QR e o código não são apagados antes de serem usados.

## QR no próprio NewPipe

Ao abrir **Subscriptions → Connect YouTube account**, o NewPipe abre um submenu com:

- **Abrir QR Code**: mostra a imagem pelo visualizador nativo do Kodi, que preserva a proporção e exibe o QR inteiro;
- **Código de ativação**: mostra o endereço e o código manual;
- **Verificar ligação agora**;
- **Cancelar código de ativação**.

O QR é gerado localmente pelo próprio add-on e abre a ligação curta de ativação do YouTube. **Não abre o SmartTube.**

## Instalação

1. Instale `plugin.video.newpipe-1.2.5-login-pendente.zip` em **Add-ons → Instalar a partir de ficheiro ZIP**.
2. Confirme a mensagem de atualização do NewPipe.
3. Volte a abrir o NewPipe. Caso o Kodi esteja aberto há muito tempo, reinicie-o uma vez para que o serviço novo seja iniciado.
4. Abra **Subscriptions** e escolha **Connect YouTube account**.

O pacote continua autónomo: não requer módulos `script.module.*` externos.
