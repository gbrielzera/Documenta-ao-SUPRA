# ExecucaoTimer

Caminho: Customização > Modelo de objetos > Processo > ExecucaoTimer

Execução de Eventos baseados em Tempo

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Atividade** | Uma Atividade de Processo corresponde a Tarefas, Subprocessos e Eventos de Processos. | [Atividade](objetos_atividade) |
| **AtividadeId** | Identificador do(a) Atividade associado(a) | Inteiro |
| **DataHoraExecucao** | Data e hora que o Timer foi executado com sucesso | Data/hora |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ExecucaoTimer Carrega(string nomePropriedade, object valorPropriedade); |
