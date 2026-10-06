# Atualização NewPipe 1.0.1 — miniaturas e páginas

Este pacote corrige a exibição que aparecia com o **logo/fanart do NewPipe** no lugar da miniatura de cada vídeo e adiciona paginação para as listas.

## O que mudou

- Cada cartão de vídeo passa a usar a miniatura direta do próprio vídeo no YouTube (`hqdefault.jpg`).
- A arte de fanart é deliberadamente limpa nos itens de vídeo, evitando que a skin reutilize a imagem de fanart do add-on.
- As listas carregam **25 vídeos por página** com a configuração padrão de **Resultados por página**.
- Quando houver mais resultados, é adicionado o item **Next page 2**, **Next page 3** e assim por diante.
- A página 2 contém os vídeos 26–50; a página 3 contém os vídeos 51–75, e assim sucessivamente.
- A navegação preserva a busca, a categoria Trending/Live, o canal, a aba do canal (Vídeos/Shorts/Live) e a playlist selecionada.

A paginação foi aplicada a buscas de vídeos, Trending, Live, vídeos do canal, playlists, feed de inscrições e histórico. Buscas de canais e de playlists também recebem o item de próxima página quando aplicável.

> A tela terá **25 cartões de vídeo** e, somente quando existir conteúdo adicional, mais um item de navegação **Next page**. Esse último não é um vídeo.

## Como atualizar no Kodi

1. Baixe `plugin.video.newpipe-1.0.1-paginacao.zip` e copie-o para uma pasta acessível pelo Kodi.
2. No Kodi, acesse **Add-ons > Instalar a partir de um arquivo ZIP**.
3. Selecione o ZIP desta atualização e aguarde a notificação de instalação/conclusão.
4. Abra o NewPipe e faça uma busca. A primeira tela deverá exibir até 25 vídeos com as respectivas miniaturas; ao final, selecione **Next page 2** para carregar a próxima faixa de resultados.
5. Caso uma tela antiga ainda apareça, abra **Configurações do NewPipe > Clear cache**, saia do add-on e abra-o novamente.

O pacote mantém as dependências do NewPipe 1.0.0 e requer o mesmo repositório Twilight0 instalado anteriormente. Se estiver fazendo uma instalação do zero, instale primeiro `repository.twilight0-2.0.2.zip` do kit anterior.

## Configuração de quantidade por página

Em **Configurações do NewPipe > Results per page**, deixe o valor em **25** para o comportamento descrito acima. A configuração continua disponível: se for alterada para outro valor, esse será o número de vídeos por página.

## Verificação rápida

- As imagens dos cartões devem ser imagens de cada vídeo, não o logotipo do NewPipe.
- A miniatura da página 1 não deve ser repetida por causa do fanart do add-on.
- Se existirem mais de 25 resultados, o fim da lista exibirá **Next page 2**.
- Ao selecionar esse item, a tela deve exibir a próxima faixa de vídeos, sem abrir novamente a escolha de tipo de busca.
