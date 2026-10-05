# TemposANO

Caminho: Customização > Modelo de objetos > Processo > TemposANO

Tempos registrados para cada solucionador em decorrência de configuração do Acordo de Nível Operacional.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DataHoraRegistro** | Data e hora em que foi gerado do registro de tempo/responsabilidade. | Data/hora |
| **OcorrenciaId** | Identificador da Ocorrência que está sendo executada. Utilizado como chave composta para o registro de execução de atividade. | Inteiro |
| **Sequencial** | Sequencial da atividade executada em uma ocorrência. | Inteiro |
| **Solucionador** | Solucionador participante da execução da atividade | [Pessoa](objetos_pessoa) |
| **SolucionadorId** | Identificador do solucionador envolvido na execução da atividade | Inteiro |
| **Tempo** | Tempo atribuído a um Solucionador na execução de uma atividade com acordo de nível operacional. Este valor é preenchido quando ocorre um encaminhamento (troca de responsabilidade), finalização da atividade ou cancelamento da atividade. | Inteiro |
| **TempoSegundos** | Complemento em segundos do tempo atribuído a um Solucionador na execução de uma atividade com acordo de nível operacional. Este valor é preenchido quando ocorre um encaminhamento (troca de responsabilidade), finalização da atividade ou cancelamento da atividade. | Inteiro |
