# NewPipe 1.0.3 — região Brasil e Trending sem viés global

A versão 1.0.3 corrige a lista mostrada no exemplo: a entrada **Trending > Music** usava a palavra inglesa `Music` ordenada por visualizações globais. Mesmo com `BR`/`pt` configurado, essa combinação favorecia os maiores mercados globais, incluindo músicas indianas.

## Correções desta versão

| Área | Comportamento anterior | Correção 1.0.3 |
|---|---|---|
| Trending > Music | Busca global `Music`, ordenada por visualizações | Categoria **Música**, com relevância e contexto Brasil/português |
| Trending > Gaming | Busca global `Gaming` | Categoria **Jogos** |
| Trending > News | Busca global `News` | Categoria **Notícias** |
| Trending > Movies | Busca global `Movies` | Categoria **Filmes** |
| Live | Termos globais em inglês | Termos em português: Música ao vivo, Notícias ao vivo, Esportes ao vivo etc. |
| Links antigos | `Music`, `Movies` e similares eram mantidos | São convertidos automaticamente para `Música`, `Filmes` e equivalentes |

O add-on continua a enviar os parâmetros usados pelo NewPipe Extractor para todas as consultas e continuações:

| Parâmetro | Valor padrão | Uso |
|---|---:|---|
| `gl` | `BR` | País do conteúdo: Brasil |
| `hl` | `pt` | Idioma de conteúdo do YouTube: português do Brasil |
| `Accept-Language` | `pt,pt;q=0.9,en;q=0.5` | Idioma preferencial da página web |

Também permanece a correção de paginação: o add-on elimina cartões repetidos, não descarta vídeos quando uma resposta secundária varia e fornece 25 vídeos por página quando o YouTube disponibilizar quantidade suficiente.

## Instalação

1. No Cinebox/Kodi, abra **Add-ons > Instalar a partir de um arquivo ZIP**.
2. Instale `plugin.video.newpipe-1.0.3-regiao-localizada.zip`.
3. Abra **NewPipe > Settings** e confirme:
   - **País do conteúdo (ISO 3166-1):** `BR`
   - **Idioma do conteúdo (código do YouTube):** `pt`
   - **Resultados por página:** `25`
4. Use **Limpar cache** uma vez e entre novamente em **Trending**.
5. Selecione **Música**, **Filmes**, **Notícias** ou outra categoria do novo menu em português. Não reutilize uma lista antiga aberta antes da atualização.

> O YouTube controla o resultado final e pode incluir artistas internacionais. A atualização remove o filtro/ordenação global que provocava o domínio de conteúdo indiano na categoria Music e passa a consultar a categoria brasileira em português.

## Referência técnica

O modelo de localização segue o [NewPipe](https://github.com/TeamNewPipe/NewPipe) e o [NewPipe Extractor](https://github.com/TeamNewPipe/NewPipeExtractor): idioma (`hl`) e país de conteúdo (`gl`) são dados distintos e devem ser inseridos em cada consulta do YouTube. Esta atualização altera somente o add-on NewPipe; o Cinebox continua sendo o ambiente Kodi para seus catálogos e outros add-ons.
