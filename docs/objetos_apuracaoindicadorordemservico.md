# ApuracaoIndicadorOrdemServico

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorOrdemServico

Apuração de Indicador de Desempenho associado a Ordens de Serviço

Este tipo herda atributos e funcionalidades do ancestral [ApuracaoIndicador](objetos_apuracaoindicador)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **GrupoTrabalho** | Grupo Trabalho | [GrupoTrabalho](objetos_grupotrabalho) |
| **GrupoTrabalhoId** | Identificador do GrupoTrabalho associado | Inteiro |
| **Pessoa** | Pessoa responsável pela Ordem de Serviço | [Pessoa](objetos_pessoa) |
| **PessoaId** | Identificador da Pessoa associada | Inteiro |
| **Servico** | Um Serviço pode ser definido como um sistema composto por Tecnologia, Facilidades, Processos e Pessoas que habilitam um processo de negócio. | [Servico](objetos_servico) |
| **ServicoId** | Identificador do Servico associado | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ApuracaoIndicadorOrdemServico Carrega(string nomePropriedade, object valorPropriedade); |
