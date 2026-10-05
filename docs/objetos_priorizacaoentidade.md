# PriorizacaoEntidade

Caminho: Customização > Modelo de objetos > Processo > PriorizacaoEntidade

Configuração de Fatores de Priorização para Entidade do sistema.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Codigo** | Código para recuperação de objetos reconhecidos pelo fabricante do software. | String |
| **Descricao** | Descrição detalhada da PriorizacaoEntidade | String |
| **Fatores** | Fatores utilizados para cálculo de Prioridade. | [Lista de FatorPrioridade](objetos_fatorprioridade) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma PriorizacaoEntidade | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | PriorizacaoEntidade Carrega(int i); |
| **Novo** | Cria um novo registro do tipo PriorizacaoEntidade | PriorizacaoEntidade Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | PriorizacaoEntidade Carrega(string nomePropriedade, object valorPropriedade); |
