# Processo

Caminho: Customização > Modelo de objetos > Processo > Processo

Um Processo é composto por uma coleção de rotinas denominadas Subprocessos. As rotinas de um Processo são especificadas por uma linguagem gráfica de mercado denominada BPMN - Business Process Management Notation. A execução de um Processo é realizada por Ordens de Serviços que são ocorrências solicitadas por um Cliente, sob responsabilidade de um Solucionador e com um Serviço associado.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Tipo de Serviço está Ativo. Quando ativo o Tipo é visível em formulários de entrada de dados para Ordens de Serviço ou Consultas diversas | Booleano |
| **ClasseNegocio** | Classe de Negócio utilizada pelo Processo. | [ClasseNegocio](enum_classenegocio) |
| **Descricao** | Descrição detalhada do Processo. Este descritivo é utilizado para nomear pastas no repositório de arquivo e por este motivo não pode conter os seguintes caracteres \\ / : > ? * " | String |
| **ExpressaoPastasAnexos** | Fórmula para caminho de pastas de Itens de Configuração anexados em Ocorrências | String |
| **ExpressaoPastasAprovacao** | Fórmula para caminho de pastas de Itens de Configuração para aprovação em Ocorrências | String |
| **FatorPrioridade** | Fator utilizado no cálculo de Prioridade | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do(a) FatorPrioridade associado(a) | Inteiro |
| **Id** | Identificador do Processo | Inteiro |
| **MacroProcesso** | Agrupamento de processos endereçados a uma área de negócio | [MacroProcesso](objetos_macroprocesso) |
| **MacroProcessoId** | Identificador do MacroProcesso associado | Inteiro |
| **Sigla** | Nome abreviado para o Processo. Este identificador pode ser utilizado por scripts para automatização de processos. | String |
| **Versoes** | Versões do Processo | [Lista de DesenhoProcesso](objetos_desenhoprocesso) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemValorFatorPrioridade** | Obtem Valor associado ao Fator de Prioridade do Processo. Se não existir uma definição de Fator de Prioridade no Processo então é retornado o valor default fornecido como parâmetro. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **ObtemAmbiente** | Recupera ambiente de funcionamento do sistema que pode ser igual a "Qualidade" ou "Produção". A configuração do ambiente é definida durante a instalação da aplicação Supravizio Server e pode ser modificado a qualquer momento pelo Configurador Supravizio Server (o usuário necessariamente precisa de acesso especial ao ambiente onde esta aplicação estiver instalada). | string ObtemAmbiente(); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Processo Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Processo | Processo Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Processo Carrega(string nomePropriedade, object valorPropriedade); |
