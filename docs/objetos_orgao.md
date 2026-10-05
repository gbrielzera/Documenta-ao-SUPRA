# Orgao

Caminho: Customização > Modelo de objetos > Recurso > Orgao

Diretoria, Gerência, Departamento ou Área que compõe a estrutura organizacional. Em um Órgão, também denominado Área, podemos associar empregados ou terceiros (lotação). Um Órgão pode possuir uma associação com outro Órgão denominado "Pai". Esta associação "pai-filho" define a hierarquia de órgãos de uma Empresa.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Órgão está Ativo | Booleano |
| **Descricao** | Texto que descreve claramente a função do Órgão. Este texto é utilizado por profissionais e clientes para busca por itens da estrutura organizacional. | String |
| **Empresa** | Empresa ao qual pertence o Órgão. Se preenchido é anulado o campo Unidade de Negócio. | [Empresa](objetos_empresa) |
| **EmpresaId** | Identificador da Empresa dona do Órgão. | Inteiro |
| **Gestor** | Gestor responsável pelo Órgão | [Pessoa](objetos_pessoa) |
| **GestorId** | Identificador do Gestor do Órgão. Esta associação é utilizada constantemente na implementação de Processos. | Inteiro |
| **Id** | Identificador do Órgão | Inteiro |
| **OrgaoPai** | Diretoria, Gerência, Departamento ou Área que compõe a estrutura organizacional. Em um Órgão, também denominado Área, podemos associar empregados ou terceiros (lotação). Um Órgão pode possuir uma associação com outro Órgão denominado "Pai". Esta associação "pai-filho" define a hierarquia de órgãos de uma Empresa. | [Orgao](objetos_orgao) |
| **OrgaoPaiId** | Identificador do Orgao pai que define a hierarquia organizacional. | Inteiro |
| **Sigla** | Nome resumido (código) utilizado para identificar um Órgão. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemSubOrgaos** | Recupera todos os Sub-órgãos do nível inferiour ou, se for executado com a opção de recursividade, recupera todos os níveis inferiores. | Venki.Supravizio.Recurso.OrgaoList ObtemSubOrgaos(bool recursivo); |
| **ObtemOrgaosPais** | Recupera todos os órgãos que estão acima na hierarquia. A recuperação é executada até que seja encontrado um órgão sem informação de órgão pai. | Venki.Supravizio.Recurso.OrgaoList ObtemOrgaosPais(); |
| **ObtemTodosGestores** | Recupera todos os gestores de órgãos ativos. Todos os objetos retornado não podem ser modificados (somente-leitura). | Venki.Supravizio.Recurso.PessoaList ObtemTodosGestores(); |
| **ObtemColaboradores** | Recupera todos os colaboradores de um órgão com possibilidade de incluir subníveis. Permite excluir ou recuperar apenas Gestores. | Venki.Supravizio.Recurso.PessoaList ObtemColaboradores(bool incluSubniveis, bool somenteGestores, bool excluiGestores); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Orgao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Orgao | Orgao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Orgao Carrega(string nomePropriedade, object valorPropriedade); |
