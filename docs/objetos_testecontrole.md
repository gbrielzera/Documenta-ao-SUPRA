# TesteControle

Caminho: Customização > Modelo de objetos > Processo > TesteControle

Ocorrências de Teste do Controle

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Controle** | Controle testado | [Controle](objetos_controle) |
| **ControleId** | Identificador do(a) Controle associado(a) | Inteiro |
| **CriterioSelecao** | Critério de seleção utilizado na realização do Teste | String |
| **Ocorrencia** | Ocorrência gerada para teste do Controle | [Ocorrencia](objetos_ocorrencia) |
| **OcorrenciaId** | Identificador da Ocorrencia associada | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | TesteControle Carrega(string nomePropriedade, object valorPropriedade); |
