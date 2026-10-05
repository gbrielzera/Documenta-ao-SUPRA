# Risco

Caminho: Customização > Modelo de objetos > Processo > Risco

Risco cadastrado na biblioteca de Riscos

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Afirmacoes** | Afirmações Financeiras relacionadas com o Risco | [Lista de RiscoAfirmacao](objetos_riscoafirmacao) |
| **AreaRisco** | Área de Risco | [AreaRisco](objetos_arearisco) |
| **AreaRiscoId** | Identificador do AreaRisco associado | Inteiro |
| **CategoriaRisco** | Categoria do Risco | [CategoriaRisco](objetos_categoriarisco) |
| **CategoriaRiscoId** | Identificador do CategoriaRisco associado | Inteiro |
| **Descricao** | Descrição detalhada do Risco | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Risco | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Risco Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Risco | Risco Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Risco Carrega(string nomePropriedade, object valorPropriedade); |
