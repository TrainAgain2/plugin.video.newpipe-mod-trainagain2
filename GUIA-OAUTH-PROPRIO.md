# NewPipe MOD — evolução da autenticação YouTube

Versões anteriores utilizaram um cliente OAuth configurado manualmente. A versão atual do NewPipe MOD utiliza o fluxo de ativação **YouTube TV**, gerando um código temporário e um QR diretamente no submenu do add-on.

## Fluxo atual

1. O NewPipe MOD obtém os dados públicos atuais do cliente YouTube TV.
2. O YouTube devolve um código temporário e o respetivo endereço de ativação.
3. O QR abre `youtube.com/qr/activate/<código>`; como alternativa, pode abrir `https://yt.be/activate` e introduzir o código manualmente.
4. Depois da autorização, o NewPipe MOD guarda somente a sessão local necessária para sincronizar a biblioteca da conta.

Não é necessário configurar ID de cliente, segredo ou projeto Google Cloud nas definições do Kodi.

Referência oficial: [iniciar sessão no YouTube numa TV](https://support.google.com/youtube/answer/3015415?hl=pt-BR).
