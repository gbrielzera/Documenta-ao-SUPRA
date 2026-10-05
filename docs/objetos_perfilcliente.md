# PerfilCliente

Caminho: Customização > Modelo de objetos > Recurso > PerfilCliente

O Perfil de Cliente pode ser utilizado para definição de privilégios do Cliente em atendimentos diversos com impacto na definição de ANS.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Texto que descreve claramente a utilização de um Perfil de Cliente. Este texto é utilizado na tela de Cadastro de Clientes para associação de Perfil com Cliente e também na tela de Ordem de Serviço para informar ao Solucionador o privilégio conferido. | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Perfil de Cliente | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | PerfilCliente Carrega(int i); |
| **Novo** | Cria um novo registro do tipo PerfilCliente | PerfilCliente Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | PerfilCliente Carrega(string nomePropriedade, object valorPropriedade); |
