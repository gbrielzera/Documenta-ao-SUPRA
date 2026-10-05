# ChangeLog

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog

Registro de modificação de um objeto.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Class** | Classe do Objeto modificado | [Class](objetos_class) |
| **ClassId** | Identificador da Classe do Objeto modificado. | Inteiro |
| **DateTime** | Data e hora da modificação | Data/hora |
| **Id** | Identificador da Modificação | Decimal |
| **Items** | Modificação de Propriedades | [Lista de ChangeItem](objetos_changeitem) |
| **KeyValue** | Chave de identificação do Objeto de Negócio modificado. | String |
| **ParentId** | Identificador da Modificação Pai. Este campo é preenchido para objetos que são Partes em associações do tipo Composition. | Inteiro |
| **TextualRepresentation** | Representação textual do registro modificado | String |
| **UserId** | Identificador do Usuário que realizou a modificação. | Inteiro |
| **Version** | Número de Versão para o registro. | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ChangeLog Carrega(string nomePropriedade, object valorPropriedade); |
