# TimeSheet

Caminho: Customização > Modelo de objetos > Processo > TimeSheet

Apontamento de Horas Trabalhadas

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Atividade** | Atividade executada durante o intervalo do Apontamento. | [Atividade](objetos_atividade) |
| **AtividadeId** | Identificador do(a) Atividade associado(a) | Inteiro |
| **DataHoraApontamento** | Data/hora em que foi feito o apontamento | Data/hora |
| **DataHoraAtualizacao** | Data/hora de última atualização do Apontamento | Data/hora |
| **DataHoraFim** | Data/hora de Fim | Data/hora |
| **DataHoraInicio** | Data/hora de início | Data/hora |
| **DuracaoMinutos** | Duração de um apontamento em minutos | Inteiro |
| **GrupoTrabalho** | Grupo de Trabalho do Solucionador no instante do Apontamento | [GrupoTrabalho](objetos_grupotrabalho) |
| **GrupoTrabalhoId** | Identfiicador do Grupo de Trabalho do Solucionador no instante em que foi realizado o apontamento | Inteiro |
| **Observacao** | Texto de Observação para detalhamento do apontamento. | String |
| **Ocorrencia** | Ocorrência associada | [Ocorrencia](objetos_ocorrencia) |
| **OcorrenciaId** | Identificador da Ocorrência de Processo associada | Inteiro |
| **Sequencial** | Sequencial do apontamento em uma Ordem de Serviço | Inteiro |
| **Tecnico** | Solucionador que realizou o Apontamento | [Pessoa](objetos_pessoa) |
| **TecnicoId** | Identificador do Solucionador associado ao apontamento | Inteiro |
| **TipoApontamento** | Tipo de Apontamento | [TipoApontamento](objetos_tipoapontamento) |
| **TipoApontamentoId** | Identificador do Tipo de Apontamento associado | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **IsApropriado** | Verifica se um apontamento está apropriado | System.Boolean IsApropriado(int idOcorrencia, int sequencial); |
| **IsAprovado** | Verifica se um apontamento está envolvido em alguma aprovação aprovada. | System.Boolean IsAprovado(int idOcorrencia, int sequencial); |
| **ValidaIntervalo** | Verifica se é possível a inserção/modificação de um apontamento levando em consideração seus conflitos. Retorna mensagem de erro se houver. Senão, retorna nulo. | System.String ValidaIntervalo(int idOcorrenciaApontamento, System.Int32 sequencialApontamento, int idPessoaTecnico, Venki.Supravizio.Recurso.FormaApontamento forma, System.DateTime inicio, System.DateTime fim, System.TimeSpan duracao); |
| **ObtemSituacao** | Indica a situação de um apontamento | System.Int32 ObtemSituacao(int idOcorrencia, int sequencial); |
| **ObtemSituacoes** | Retorna um array de strings com {OcorrenciaId}_{Sequencial}_{SituacaoTimeSheet} | System.String[] ObtemSituacoes(TimeSheetKey key); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | TimeSheet Carrega(string nomePropriedade, object valorPropriedade); |
