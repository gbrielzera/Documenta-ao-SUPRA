# ApontamentoResponsavel

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel

Mantém histórico de Responsáveis por Item de Processo

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DataHoraInicio** | Data e hora de início para o período no qual o Solucionador foi responsável | Data/hora |
| **ExplicacaoAtor** | Texto explicativo sobre o cálculo de um ator na Ordem de Serviço. | String |
| **Ocorrencia** | Ocorrências de Processos | [Ocorrencia](objetos_ocorrencia) |
| **OcorrenciaId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | Inteiro |
| **Responsavel** | Pessoa que recebeu a ocorrência em sua fila (Destinatário do encaminhamento). | [Pessoa](objetos_pessoa) |
| **ResponsavelAtendePapel** | Indica que o usuário responsável atendeu aos requisitos de papeis definidos em processo. | Booleano |
| **ResponsavelId** | Identificador do Solucionador Responsável | Inteiro |
| **Sequencial** | Sequencial de responsabilidade para uma determinada Ordem de Serviço. | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ApontamentoResponsavel Carrega(string nomePropriedade, object valorPropriedade); |
