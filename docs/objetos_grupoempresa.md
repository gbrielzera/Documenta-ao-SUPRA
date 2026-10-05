# GrupoEmpresa

Caminho: Customização > Modelo de objetos > Recurso > GrupoEmpresa

Grupo empresarial controlador de empresas cadastradas no sistema. Na aplicação de Autoatendimento um grupo pode ser utilizado para restringir a seleção de pessoas do grupo onde está cadastrado o usuário conectado, evitando que um usuário acesse o cadastro de pessoas de outras empresas.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Grupo Empresarial está Ativo. | Booleano |
| **Descricao** | Nome do Grupo Empresarial | String |
| **Id** | Número sequencial gerado por sistema para Identificar um Grupo Empresarial | Inteiro |
| **Sigla** | Nome resumido utilizado para identificar um Grupo Empresarial. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | GrupoEmpresa Carrega(int i); |
| **Novo** | Cria um novo registro do tipo GrupoEmpresa | GrupoEmpresa Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | GrupoEmpresa Carrega(string nomePropriedade, object valorPropriedade); |
