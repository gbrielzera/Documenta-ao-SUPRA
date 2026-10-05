# Arquitetura e requisitos

Caminho: Apresentação > Arquitetura e requisitos

A arquitetura da solução Supravizio possui uma arquitetura baseada em uma camada cliente e uma camada servidora:

Arquitetura da solução

Na tabela abaixo podemos verificar as principais características e requisitos de cada componente da arquitetura Supravizio:

### Na Camada Servidora

Na camada servidora a solução é composta por duas aplicações sendo executadas em um servidor utilizando o Microsoft IIS e um serviço Windows. Não é obrigatória a instalação de todas as aplicações em um mesmo servidor.

| **Aplicação** | **Características funcionais** | **Requisitos** |
|---|---|---|
| **Supravizio Server** | - Aplicação Windows Service contendo um socket Server com porta configurável; - Faz acesso ao servidor de arquivos para escrita e leitura em repositório de arquivos parametrizável; - Pode acessar servidor de emails via POP3 e SMTP; - Pode ser instalado em servidores virtuais; | - Processador Intel Dual Core (ou similar) com 4GB de memória. O produto possui instaladores para 32 e 64 bits; - Sistema operacional Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows Server 2008, Windows Server 2008 R2, Windows Server 2012 ou Windows Server 2014; - Client Banco de Dados Oracle 11g (Versão 11.2.0.3.0) ou SQL Server 2005, 2008, 2012 ou 2014; - Windows Powershell 1.0 ou superior; - Microsoft .NET Framework versões 3.5, 4.0; |
| **Supravizio Web** | - Utilizado por solucionadores e pelo aplicativo Windows; - Faz acesso direto ao banco de dados; - Aplicação Web contendo a funcionalidade webservice; - Pode ser instalado em servidores virtuais; - Faz acesso ao servidor de arquivos para escrita e leitura em repositório de arquivos parametrizável; | - Processador Intel Dual Core (ou similar) com 4GB de memória. O produto possui instaladores para 32 e 64 bits; - Sistema operacional Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows Server 2008, Windows Server 2008 R2, Windows Server 2012 ou Windows Server 2014; - Client Banco de Dados Oracle 11g (Versão 11.2.0.3.0) ou SQL Server 2005, 2008, 2012 ou 2014; - Servidor web IIS 7.0 ou superior; - Windows Powershell 1.0 ou superior; - Microsoft .NET Framework versões 3.5, 4.0; |

### Nas Estações Clientes

### Nas estações clientes os solucionadores e solicitantes contarão com um navegador (ver lista completa ao fim deste tópico) para a abertura de solicitações e a execução de processos. Os analistas de processos e administradores contarão com um client Windows para a criação e mudança em processos ou administração de recursos do sistema.

| **Aplicação** | **Características funcionais** | **Requisitos** |
|---|---|---|
| **Supravizio Windows** | - Utilizado por solucionadores, analistas de processos e administradores; - Não requer instalação de cliente de banco de dados. Os dados são recuperados e persistido a partir da camada servidora; - Existe um mecanismo de atualização automática; - Utiliza conexão com o Supravizio Web; - Faz acesso ao servidor de arquivos via compartilhamento ou transferência; - Pode ser instalado em máquinas virtuais ou servidores de virtualização de clients; | - Processador Intel Pentium Dual Core (ou similar) com 1 GB de memória. O produto possui instaladores para arquiteturas 32 bits e 64 bits; - Sistema operacional Windows Vista ou Windows 7; - Microsoft .NET Framework versões 3.5, 4.0; |
| **Cliente do Supravizio Web** | - Utilizado por solucionadores e gestores de processos; - Requer apenas browser (navegador web) para acesso ao sistema. | - Veja [tabela de compatibilidade de navegadores](pre_requisitos) |

### Outros Requisitos

- Usuário de e-mail para envio de mensagens via SMTP ou Exchange e recebimento via POP3, IMAP ou Exchange;
- Usuário de rede com acesso de escrita em pasta do servidor de arquivos (repositório de arquivos do Supravizio);
- Usuário de banco de dados com permissão de criação de novas tabelas, alteração (ALTER TABLE) em todas as tabelas do Supravizio e criação/alteração de Constraints. Permissão também para a execução de Procedures;
- Se o banco de dados for Oracle, o esquema deve obrigatoriamente receber o nome SV.
- Podem existir processos para manutenção automática do **Active Directory** (desbloqueio, inclusão de usuário em grupo etc), então será necessário um usuário de sistema operacional membro do grupo **Account Operator**.** Importante**: Por questões de segurança, um membro do grupo Account Operator não pode criar ou modificar contas de administradores do domínio, ou modificar sua própria conta. No caso de **OpenLDAP**, o usuário configurado no aplicativo também precisa possuir autorização para realizar modificações em objetos e propriedades.
- Para conexão com o banco de dados OCS, é necessário a instalação do Provider ADO.NET MySql versão 6.8.3, que pode ser obtido no endereço: [http://dev.mysql.com/downloads/connector/net/](http://dev.mysql.com/downloads/connector/net/).
- Caso o servidor no qual a aplicação esteja sendo instalado possua instalado .NET Framework 4.5, será necessário que estejam instaladas todas as atualizações disponibilizadas pelo fabricante. **Nestes casos, é necessário que o Application Pool do IIS esteja configurado para modo Classic**.

## Tabela de Compatibilidade do Supravizio Web

Segue abaixo a tabela de compatibilidade de versões de navegadores que podem ser utilizados para o Supravizio Web:

|  | Internet Explorer | Google Chrome | Firefox | Safari | Opera |
|---|---|---|---|---|---|
|  | 8 | 9 | 10 | 11 | 4 ou superior | 3.5 ou superior | 5.1 ou superior | 11.1 ou superior |
| Visualização gráfica de fluxos |  |  |  |  |  |  |  |  |
| Dashboard |  |  |  |  |  |  |  |  |
| Todas as Demais Funcionalidades |  |  |  |  |  |  |  |  |

### Tabela de Compatibilidade de Recursos no Supravizio Web

* Necessita instalação do Microsoft .NET Framework 4.5.1 e Pool de Aplicações configurado em modo **Classic**
