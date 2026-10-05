# TipoApontamento

Caminho: Customização > Modelo de objetos > Recurso > TipoApontamento

Um Tipo de Apontamento pode ser utilizado no cadastro de Contratos para definir um fator aplicado a um valor/recurso também registrado no contrato.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição do Tipo de Apontamento | String |
| **Id** | Identificador do Tipo de Apontamento | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | TipoApontamento Carrega(int i); |
| **Novo** | Cria um novo registro do tipo TipoApontamento | TipoApontamento Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | TipoApontamento Carrega(string nomePropriedade, object valorPropriedade); |
