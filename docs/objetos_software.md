# Software

Caminho: Customização > Modelo de objetos > Ativos > Software

Itens de Configuração do tipo 'Licenças de Software'.

Este tipo herda atributos e funcionalidades do ancestral [ItemConfiguracao](objetos_itemconfiguracao)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CopiasLicenciadas** | Número de cópias licenciadas | Inteiro |
| **InstalacoesAuditadas** | Instalações auditadas | Inteiro |
| **ReferenciaLicenca** | Dados de referência para o Licenciamento do Software | String |
| **Versao** | Versão do Software | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Software Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Software | Software Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Software Carrega(string nomePropriedade, object valorPropriedade); |
