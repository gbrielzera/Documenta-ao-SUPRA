# Conhecimento

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento

Artigo de Base de Conhecimento

Este tipo herda atributos e funcionalidades do ancestral [ItemConfiguracao](objetos_itemconfiguracao)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AplicacaoConhecimentoServico** | Regras de utilização do artigo em função de Serviços e Tipos de Serviços. Estas regras influenciarão o mecanismo de recuperação de artigos durante a busca manual ou automática. | [Lista de AplicacaoConhecimentoServico](objetos_aplicacaoconhecimentoservico) |
| **PalavrasChave** | Palavras Chave para pesquisa | String |
| **RestricoesAcesso** | Composição entre permissão e conhecimento | [Lista de PermissaoConhecimentoPapel](objetos_permissaoconhecimentopapel) |
| **Sumario** | Sumário | String |
| **SumarioTexto** | Sumário em forma de texto, sem as TAGs html | String |
| **Titulo** | Título | String |
| **Topicos** | Tópicos que compõem o artigo. Estes tópicos são ordenados pelo sequencial cadastrado do tipo de artigo. | [Lista de Topico](objetos_topico) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemConhecimento** | Retorna uma lista de dados referente a base de conhecimento armazenada em artefatos e ordens de serviço | System.Collections.ArrayList ObtemConhecimento(string criterio, Supravizio.Processo.Servico servico, Supravizio.Configuracao.ClasseConfiguracao configuracao,Supravizio.Processo.ClasseServico classeServico, bool pesquisaOs, bool pesquisaArtigos); |
| **ObtemConhecimento** | Retorna uma lista de dados referente a base de conhecimento armazenada em artefatos e ordens de serviço | System.Collections.ArrayList ObtemConhecimento(string criterio); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Conhecimento Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Conhecimento | Conhecimento Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Conhecimento Carrega(string nomePropriedade, object valorPropriedade); |
