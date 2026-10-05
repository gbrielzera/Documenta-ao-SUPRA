# ChargeBack

Caminho: Customização > Modelo de objetos > Recurso > ChargeBack

Cobrança por uso de Ativo ou serviço prestado.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ano** | Ano competência | Inteiro |
| **Areas** | Itens apurados para o Charge-back | [Lista de ChargeBackOrgao](objetos_chargebackorgao) |
| **DataHoraProcessamento** | Data e hora de processamento do Charge-back | Data/hora |
| **HistoricoOrgao** | Histórico de estrutura organizacional na ocasião do processamento do Charge-back. | [Lista de HistoricoOrgao](objetos_historicoorgao) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | Inteiro |
| **Mes** | Mês competência | Inteiro |
| **Publicado** | Indica que os dados do Charge-back são públicos para áreas Clientes na aplicação de Autoatendimento | Booleano |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ChargeBack Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ChargeBack | ChargeBack Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ChargeBack Carrega(string nomePropriedade, object valorPropriedade); |
