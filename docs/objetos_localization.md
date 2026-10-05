# Localization

Caminho: Customização > Modelo de objetos > Utilitários > Localization

Localização de objetos

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Class** | Classe do objeto de negócio localizado. | [Class](objetos_class) |
| **ClassId** | Identificador da Classe de Negócio do objeto localilzado. | Inteiro |
| **Culture** | Cultura associada com a localização. | [Culture](objetos_culture) |
| **CultureId** | Identificador da Cultura associada com a localização. | Inteiro |
| **Id** | Identificador do objeto de negócio localizado | Inteiro |
| **Property** | Propriedade localizada | [Property](objetos_property) |
| **PropertyId** | Identificador do(a) Property associado(a) | Inteiro |
| **TextualRepresentation** | Representação textual do registro localizado | String |
| **TextValue** | Texto localizado | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Localization Carrega(string nomePropriedade, object valorPropriedade); |
