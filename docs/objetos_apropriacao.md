# Apropriacao

Caminho: Customização > Modelo de objetos > Processo > Apropriacao

Apropriação de horas trabalhadas

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ApontamentosApropriados** | Apontamentos Apropriados | [Lista de ApontamentoApropriado](objetos_apontamentoapropriado) |
| **DataHoraApropriacao** | Data/Hora da Apropriação | Data/hora |
| **Id** | Identificador da Apropriação | Inteiro |
| **Pessoa** | Pessoa | [Pessoa](objetos_pessoa) |
| **PessoaId** | Identificador da Pessoa associada | Inteiro |
| **Referencia** | Referência da Apropriação | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **PermiteEdicaoApontamentosSeApropriacaoEmAprovacao** | Permite a edição de apontamentos apropriados em uma determinada apropriação se esta não estiver presente em alguma aprovação que foi aprovada por algum aprovador. | System.Boolean PermiteEdicaoApontamentosSeApropriacaoEmAprovacao(int idApropriacao); |
| **IsApropriacaoEnvolvidaAprovacao** | Verifica se a apropriação está envolvida me alguma aprovação, independente de situação do assunto aprovação. | System.Boolean IsApropriacaoEnvolvidaAprovacao(int idApropriacao); |
| **DesapropriaApontamento** | Retira um apontamento de uma apropriação, dado o TimeSheet e a Apropriação. | void DesapropriaApontamento(int idOcorrenciaTimesheet, int sequencialTimeSheet); |
| **DesapropriaApontamentos** | Retira apontamentos de uma determinada apropriação. | void DesapropriaApontamentos(int idApropriacao); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Apropriacao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Apropriacao | Apropriacao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Apropriacao Carrega(string nomePropriedade, object valorPropriedade); |
