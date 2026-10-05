# Empresa

Caminho: Customização > Modelo de objetos > Recurso > Empresa

Uma Empresa é uma entidade composta por um ou mais órgãos onde estão lotadas pessoas. Uma empresa também pode pertencer a um grupo de empresas. Na aplicação de Autoatendimento empresas são utilizadas para restringir buscas por pessoas. Na tela de substitutos, por exemplo, são listadas apenas as pessoas lotadas na empresa do usuário conectado. Porém, se a empresa do usuário conectado faz parte de um grupo de empresas então são listadas todas as pessoas do mesmo grupo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que a Empresa está ativa | Booleano |
| **Descricao** | Nome da Empresa | String |
| **FatorPrioridade** | Fator utilizado para cálculo de Prioridade em Ocorrências. | [FatorPrioridade](objetos_fatorprioridade) |
| **FatorPrioridadeId** | Identificador do Fator de Prioridade utilizado em cálculos de Prioridade. | Inteiro |
| **GrupoEmpresaId** | Identificador do Grupo de Empresas ao qual pertence a Empresa | Inteiro |
| **GrupoEmpresas** | Grupo Empresarial que controla a Empresa | [GrupoEmpresa](objetos_grupoempresa) |
| **Id** | Número sequencial gerado por sistema para identificar uma Empresa | Inteiro |
| **Sigla** | Nome resumido utilizado para identificar uma Empresa | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemValorFatorPrioridade** | Obtem Valor do Fator de Prioridade da Empresa. Se não existir um Fator associado então retorna o valor default fornecido como parâmetro. | System.Int32 ObtemValorFatorPrioridade(System.Int32 valorDefault); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Empresa Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Empresa | Empresa Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Empresa Carrega(string nomePropriedade, object valorPropriedade); |
