# Objeto AD

Caminho: Recursos Avançados > Objeto AD

O objeto AD é um utilitário contendo funções utilizadas em scripts Python para acesso ao repositório de Active Directory.

Este objeto possui os seguintes métodos:

**Funções:**

| **Nome** | **Descrição** |
|---|---|
| **AddUserToGroup**(string username, string group) | Adiciona um usuário na lista de membros de um grupo do serviço de diretório. Se o usuário já faz parte da lista de membros do grupo então nenhuma ação é executada e a rotina retorna o valor Falso. Utilizando grupos do serviço de diretório podemos implementar rotinas diversas tais como acesso a pastas de rede, inclusão em listas de distribuição de emails, permissionamentos de sistemas etc. |
| **AuthenticateUser**(string username, string password) | Valida usuário e senha no serviço de diretório. A validação é realizada no domínio parametrizado no sistema. |
| **CreateGlobalGroup**(string name, string ou, bool security, string managedby, string description) | Cria um grupo do tipo global no serviço de diretório. Grupos globais são grupos que podem receber permissões de acesso em recursos como pastas compartilhadas, impressoras, etc., de qualquer domínio. |
| **CreateLocalGroup**(string name, string ou, bool security, string managedby, string description) | Cria um grupo do tipo local. |
| **CreateUniversalGroup**(string name, string ou, string managedby, string description) | Cria um grupo do tipo Universal. |
| **CreateUser**(string username, string ou, string firstName, string lastName, string employeeID, string displayName) | Cria uma conta de usuário no servido de diretório. |
| **DisableUser**(string username) | Desabilita uma conta de usuário no serviço de diretório. |
| **GroupExists**(string group) | Verifica se existe no serviço de diretório o grupo fornecido como parâmetro. |
| **RemoveUser**(string username) | Remove uma conta de usuário do serviço de diretório. |
| **RemoveUserFromGroup**(string username, string group) | Retira um usuário da lista de membros um grupo do serviço de diretório. |
| **ResetUser**(string username, string password) | Troca e desbloqueia a senha de um usuário do serviço de diretório. |
| **ResetUser**(string username, string password, bool changepasswordnextlogon) | Troca e desbloqueia a senha de um usuário do serviço de diretório. Permite também solicitar a troca de senha no primeiro logon do usuário. |
| **UnLockUser**(string username) | Desbloqueia um usuário no serviço de diretório. |
| **UserExist**(string username) | Verifica se usuário existe no serviço de diretório. |
| **UserExistsInGroup**(string username, string groupname) | Verifica se o usuário está contido na lista de membros de um grupo do serviço de diretório. |
| **UserIsDisabled**(string username) | Verifica no serviço de diretório se o usuário fornecido como parâmetro está desabilitado no serviço de diretório. |
| **UserIsLocked**(string username) | Verifica no serviço de diretório se o usuário fornecido como parâmetro está travado. |
| **UserReadProperty**(string username, string property) | Realiza a leitura de uma determinada propriedade de um usuário do serviço de diretório. |
| **UserWriteProperty**(string username, string property, int value) | Altera uma propriedade (tipo numérico) de um usuário no serviço de diretório. |
| **UserWriteProperty**(string username, string property, string value) | Altera uma propriedade (tipo texto) de um usuário no serviço de diretório. |
