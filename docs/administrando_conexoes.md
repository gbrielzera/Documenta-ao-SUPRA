# Administrando Conexões Ativas

Caminho: Guia para Administradores > Roteiro de implantação > Importando licença > Administrando Conexões Ativas

O licenciamento no Supravizio é baseado no uso de licenças concorrentes. Isso significa que em um determinado instante são admitidos usuários conectados na quantidade indicada no campo **Quantidade de usuários**. Esta contabilização é realizada a cada novo login realizado por um usuário no Supravizio, somando a nova conexão com as conexões existentes. Esta nova conexão não é bloqueada, possibilitando ao administrador do sistema verificar a real demanda de uso do sistema.

O uso de licenças no Supravizio pode ser contabilizado através do relatório **Demonstrativo de uso de Licenças** (no menu principal acesse **Relatórios | Demonstrativo de uso de Licenças**):

**Relatório - Demonstrativo de uso de Licenças**

As principais informações deste relatório são:

- **Usuários conectados**

Quantidade de usuários conectados em um determinado momento. Esta verificação ocorre a cada login efetuado no Supravizio, somando a nova conexão com as conexões ativas.

- **Quantidade de ocorrências**

Indica a quantidade de ocorrências de conexões simultâneas na quantidade indicada na coluna **Usuários conectados**.

Caso exceda o número de conexões concorrentes e exista o caso em que o usuário, de alguma forma, não finalizou o uso do sistema (por exemplo, desligamento forçado, queda de energia, ou qualquer outro problema que possa impedir a finalização normal da sessão), é possível "matar" a sessão que permanece aberta através de usuários com perfil de Administrador (ou até mesmo o usuário Admin). O usuário Admin deve receber uma atenção especial pois mesmo que o sistema tenha atingido o limite de usuários concorrentes conectados, o Admin pode se conectar (ele também é contabilizado, porém tem permissão de passar pelo limite da licença).

O usuário poderá consultar (desde que possua perfil de acesso configurado para esta consulta) as conexões ativas no Supravizio através da tela de Gerenciamento de Ambiente (Utilitários | Gerenciamento de ambiente) selecionando Conexões ativas na árvore:

Conexões ativas

É possível através desta tela eliminar uma conexão ativa selecionando esta na tabela de conexões ativas e clicando no botão "Matar Sessão".
