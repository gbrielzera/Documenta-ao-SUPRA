# AfirmacaoFinanceira

Caminho: Customização > Modelo de objetos > Processo > AfirmacaoFinanceira

Afirmações Financeiras

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do AfirmacaoFinanceira | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um AfirmacaoFinanceira | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | AfirmacaoFinanceira Carrega(int i); |
| **Novo** | Cria um novo registro do tipo AfirmacaoFinanceira | AfirmacaoFinanceira Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | AfirmacaoFinanceira Carrega(string nomePropriedade, object valorPropriedade); |
