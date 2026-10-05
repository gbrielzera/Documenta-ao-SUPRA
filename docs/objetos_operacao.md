# Operacao

Caminho: Customização > Modelo de objetos > Processo > Operacao

Uma Operação define uma Ação que pode ser configurada em uma Atividade de Processo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Codigo** | Código da Operação | String |
| **Descricao** | Descrição detalhada da Operacao | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Operacao | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Operacao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Operacao | Operacao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Operacao Carrega(string nomePropriedade, object valorPropriedade); |
