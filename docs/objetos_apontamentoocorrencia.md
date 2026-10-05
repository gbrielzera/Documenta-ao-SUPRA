# ApontamentoOcorrencia

Caminho: Customização > Modelo de objetos > Processo > ApontamentoOcorrencia

Apontamento genérico para Ocorrências de Processo

Este tipo herda atributos e funcionalidades do ancestral [Apontamento](objetos_apontamento)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ocorrencia** | Ocorrência associada | [Ocorrencia](objetos_ocorrencia) |
| **OcorrenciaId** | Identificador da Ocorrência associada | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ApontamentoOcorrencia Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ApontamentoOcorrencia | ApontamentoOcorrencia Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ApontamentoOcorrencia Carrega(string nomePropriedade, object valorPropriedade); |
