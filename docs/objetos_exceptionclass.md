# ExceptionClass

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass

Uma Exceção representa uma situação de erro verificada e documentada pelo sistema. Neste cadastro um usuário especial do sistema, denominado Administrador, pode customizar mensagens exibidas em situações de erro. Nesta customização é possível a utilização de propriedades na classe de negócio associada (veja o conteúdo da classe no Dicionário de Classes).

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Action** | Orientação para o Usuário para resolução do problema. O descritivo da ação pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | String |
| **Cause** | Descritivo da Causa do Erro. Este descritivo pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | String |
| **Class** | Classe de Negócio que implementa objeto de exceção para o erro. Esta classe mantém propriedades que podem ser utilizadas na formação de campos diversos da exceção: Mensagem, Causa, Efeito e Ação. | [Class](objetos_class) |
| **ClassId** | Identificador da Classe associada | Inteiro |
| **Code** | Código identificador do erro. | String |
| **Effect** | Efeito que o Erro possa ter provocado no sistema. O descritivo do efeito pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | String |
| **Id** | Identificador da Exceção | Inteiro |
| **Message** | Mensagem que é exibida para o usuário na ocorrência do erro. Esta mensagem pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | String |
| **OriginalAction** | Conteúdo do campo Ação gerado pelo fabricante deste software e disponível para reversão de texto customizado. | String |
| **OriginalCause** | Conteúdo do campo Causa gerado pelo fabricante deste software e disponível para reversão de texto customizado. | String |
| **OriginalEffect** | Conteúdo do campo Efeito gerado pelo fabricante deste software e disponível para reversão de texto customizado. | String |
| **OriginalMessage** | Conteúdo do campo Mensagem gerado pelo fabricante deste software e disponível para reversão de texto customizado. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ExceptionClass Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ExceptionClass | ExceptionClass Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ExceptionClass Carrega(string nomePropriedade, object valorPropriedade); |
