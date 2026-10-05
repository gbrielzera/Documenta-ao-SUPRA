# FrequenciaControle

Caminho: Customização > Modelo de objetos > Processo > FrequenciaControle

Frequências de testes ou execução de Controles

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do FrequenciaControle | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um FrequenciaControle | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | FrequenciaControle Carrega(int i); |
| **Novo** | Cria um novo registro do tipo FrequenciaControle | FrequenciaControle Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | FrequenciaControle Carrega(string nomePropriedade, object valorPropriedade); |
