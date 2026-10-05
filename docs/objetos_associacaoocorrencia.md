# AssociacaoOcorrencia

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia

Estabelece Associações entre Ocorrências de Processo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Alvo** | Ocorrência Alvo da Ocorrência. | [Ocorrencia](objetos_ocorrencia) |
| **AlvoId** | Identificador da Ocorrência Alvo na Associação. | Inteiro |
| **Associacao** | Definição da Associação | [Associacao](objetos_associacao) |
| **AssociacaoId** | Identificador do Associacao associado | Inteiro |
| **AtividadeGeradora** | Atividade do tipo Subprocesso ou Link final que gerou a associação entre as ocorrências | [Atividade](objetos_atividade) |
| **AtividadeGeradoraId** | Identificador da Atividade do tipo Subprocesso ou Link final que gerou a associação. | Inteiro |
| **Autor** | Pessoa que estabeleceu a Associação. | [Pessoa](objetos_pessoa) |
| **AutorId** | Identificador da Pessoa que estabeleceu a Associação. | Inteiro |
| **DataHoraAssociacao** | Data e hora em que foi estabelecida a Associação. | Data/hora |
| **Fonte** | Ocorrência Fonte da Associação. | [Ocorrencia](objetos_ocorrencia) |
| **FonteId** | Identificador da Ocorrência Fonte da Associação. | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | AssociacaoOcorrencia Carrega(string nomePropriedade, object valorPropriedade); |
