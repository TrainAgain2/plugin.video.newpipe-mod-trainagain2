# Corrigir o nome “kodi11” na autenticação Google

O texto que a Google mostra — por exemplo, **“para continuar para kodi11”** — não vem do QR, do Kodi nem do nome do cliente OAuth no NewPipe.

Ele é a **marca (Branding) do projeto Google Cloud** associado ao Client ID que emitiu o código.

> Dar ao cliente o nome interno “NewPipe Kodi” não muda a tela de autorização. O nome visto pelo utilizador vem de **Google Auth Platform → Branding → App name**.

## Para usar o novo projeto

1. Abra o projeto Google Cloud novo, não o projeto antigo chamado `kodi11`.
2. Em **Google Auth Platform → Branding**, defina o **Nome do app** como `NewPipe Kodi` (ou o nome desejado) e salve/publice conforme a sua configuração permitir.
3. Em **Google Auth Platform → Data Access**, mantenha o escopo `https://www.googleapis.com/auth/youtube.readonly`.
4. Em **Google Auth Platform → Clients**, crie ou use o Client ID pertencente a esse projeto novo.
5. No NewPipe, em **Configurações → Conta do YouTube**, substitua o **ID do cliente OAuth Google (TV)** e o **segredo** pelos valores desse cliente novo.
6. Escolha **Fazer login no YouTube** para gerar outro QR.

## Alteração no NewPipe 1.3.5

Esta versão removeu todo fallback para Client IDs antigos e a rota específica do YouTube TV. Se o ID configurado for inválido, o NewPipe apresenta erro em vez de trocar silenciosamente para outro projeto. O QR abre a página oficial Google Device e pede o código exibido no submenu.

Fontes oficiais Google:

- [Gerir a marca da aplicação OAuth](https://support.google.com/cloud/answer/15549049?hl=pt-BR)
- [Gerir clientes OAuth](https://support.google.com/cloud/answer/15549257?hl=pt-BR)
