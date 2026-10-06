# Subscrições do YouTube — NewPipe 1.4.0

O NewPipe 1.4.0 usa o mesmo formato de ativação YouTube TV usado pelo SmartTube. Não requer microG nem a criação/configuração de um cliente OAuth no Google Cloud.

## Ativação

1. Abra **Configurações → Conta do YouTube → Fazer login no YouTube**.
2. Escolha **Abrir QR Code (YouTube TV)** para digitalizar o QR ou abra `https://yt.be/activate` e informe o código apresentado.
3. Autorize a sua conta Google.
4. Espere a sincronização automática ou selecione **Verificar ligação agora**.

O QR é sempre criado com o código atual, na forma `youtube.com/qr/activate/<código>`. Cada código novo cria também uma imagem QR nova no perfil do add-on, portanto o Kodi não reutiliza a miniatura de um código anterior.

## Dados sincronizados

A sincronização importa os canais subscritos pela conta e preserva canais que já tenham sido adicionados localmente. O feed de subscrições continua a usar o catálogo público do NewPipe para listar vídeos recentes dos canais guardados.

## Terminar sessão

**Terminar sessão do YouTube** apaga apenas os tokens e o código pendente armazenados pelo NewPipe. Não remove canais no YouTube nem modifica quaisquer definições da conta Google.
