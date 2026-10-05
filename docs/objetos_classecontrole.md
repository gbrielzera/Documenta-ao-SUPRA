# ClasseControle

Caminho: Customização > Modelo de objetos > Processo > ClasseControle

Classificação de Controles

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Area** | Área | [AreaRisco](objetos_arearisco) |
| **AreaId** | Identificador da Área | Inteiro |
| **CategoriaControle** | Categoria de Riscos e Controles | [CategoriaRisco](objetos_categoriarisco) |
| **CategoriaControleId** | Identificador da Categoria | Inteiro |
| **Descricao** | Descrição detalhada do ClasseControle | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseControle | Inteiro |
| **Riscos** | Riscos padrão para Controles deste tipo | [Lista de RiscoClasseControle](objetos_riscoclassecontrole) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ClasseControle Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ClasseControle | ClasseControle Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ClasseControle Carrega(string nomePropriedade, object valorPropriedade); |
