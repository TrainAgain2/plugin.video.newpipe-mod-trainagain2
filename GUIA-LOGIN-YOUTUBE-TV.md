# NewPipe 1.4.8 — conta YouTube e menus

Esta versão reorganiza a área autenticada para seguir a estrutura de navegação do add-on **YouTube para Kodi**, mantendo o login por código/QR compatível com **YouTube TV / SmartTube**.

## Menus da conta

No menu inicial, abra **A minha conta do YouTube**. Depois do login e de uma sincronização, encontrará:

| Menu | Conteúdo |
|---|---|
| **As minhas subscrições** | Vídeos do feed de subscrições da conta YouTube. |
| **Canais subscritos** | Canais importados da conta; também preserva canais subscritos manualmente no NewPipe. |
| **Ver mais tarde** | Lista da conta quando disponível e lista local criada pelo menu de contexto **Adicionar a Ver mais tarde**. |
| **Playlists guardadas** | Playlists da conta quando o YouTube TV as retornar, mais os favoritos locais do NewPipe. |
| **Histórico de reprodução** | Histórico da conta quando disponível; sem uma cópia de conta, mostra o histórico local. |
| **Sincronizar subscrições do YouTube** | Atualiza o instantâneo local dos menus acima. |
| **Terminar sessão do YouTube** | Remove apenas o token e o instantâneo local do Kodi. Não altera a conta Google. |

## Passos para usar

1. Abra **A minha conta do YouTube**.
2. Se a conta ainda não estiver ligada, selecione **Fazer login no YouTube** e aprove o código em `yt.be/activate` ou pelo QR.
3. Depois de a página Google informar que o dispositivo está ligado, volte ao Kodi.
4. Selecione **Sincronizar subscrições do YouTube** e aguarde o resumo, por exemplo: `12 canais, 48 vídeos`.
5. Abra os menus de vídeos, canais, Ver mais tarde, playlists ou histórico.

Na sincronização, o add-on seleciona a identidade pessoal ou de marca ativa pelo endpoint interno de contas do YouTube TV — o mesmo passo usado pelo SmartTube — antes de ler a biblioteca. Assim, a subscrição não é consultada como conta anónima.

## Correção dos canais subscritos

Na versão **1.4.7**, a pasta **Canais subscritos** passa a interpretar a resposta atual do YouTube TV corretamente. O serviço TV retorna cada canal como uma aba `FEsubscriptions` e guarda o identificador real do canal (`UC…`) no parâmetro autenticado dessa aba — o mesmo formato utilizado pelo SmartTube. A atualização agora extrai esse ID, o nome e o avatar do canal para montar a lista no Kodi.

Depois de instalar a versão 1.4.7, entre em **A minha conta do YouTube** e execute uma vez **Sincronizar subscrições do YouTube**. Em seguida, **Canais subscritos** deverá mostrar a lista de canais; abrir um canal carrega os vídeos pelo visualizador normal do NewPipe.

## Fotos de perfil redondas

A versão **1.4.8** mostra a foto real de cada canal, em vez do ícone genérico de pasta do Kodi. Durante a sincronização, o add-on corrige os endereços de imagem fornecidos pelo YouTube e guarda uma cópia circular com cantos transparentes no perfil local do NewPipe. Assim, a foto aparece redonda na lista de **Canais subscritos**.

Após instalar, use **Sincronizar subscrições do YouTube** uma vez para atualizar as imagens já guardadas. Caso o componente opcional de imagens do Kodi não esteja disponível, a foto original continua a ser apresentada, sem impedir a sincronização ou a abertura dos canais.

> A sincronização é **manual e explícita**. Abrir uma pasta não faz uma chamada de rede autenticada, para evitar bloqueios ou encerramento do Kodi quando o YouTube TV está lento.

## O que não é usado

A sincronização usa o endpoint interno autenticado do **YouTube TV** (`youtubei/v1/browse`) e não utiliza:

- YouTube Data API v3;
- projeto/chaves Google Cloud configuradas no Kodi;
- microG;
- `plugin.video.youtube`;
- um add-on de dependência externo.

O token e os instantâneos da biblioteca ficam somente no perfil local do add-on.

## Referências

- [SmartTube — código público](https://github.com/yuliskov/SmartTube)
- [Plugin YouTube para Kodi — código público](https://github.com/anxdpanic/plugin.video.youtube)
- [Ajuda oficial do YouTube — iniciar sessão numa TV](https://support.google.com/youtube/answer/3015415?hl=pt-BR)
