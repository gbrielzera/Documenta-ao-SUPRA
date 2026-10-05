# HARDWARE

Caminho: Customização > Modelo de dados > Ativos > HARDWARE

Itens de Configuração do tipo 'Equipamento'

Por se tratar de um tipo herdado de ItemConfiguracao, a tabela HARDWARE possui uma chave estrangeira apontando para a tabela [ITEM](dados_item).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **ETIQUETA_ID** | Número da Etiqueta de Identificação do Equipamento pela equipe de suporte. Este número pode ser utilizado pelo Solucionador durante o atendimento de um chamado. | varchar(500) | varchar(500) | Sim |
| **PATRIMONIO** | Identificação de Patrimonio | varchar(100) | varchar(100) | Sim |
| **ID_LOCAL** | Identificador da localização do Equipamento | int | number(6,0) | Sim |
| **CODIGO_OCS** | Código do hardware original do banco de dados OCS | varchar(500) | varchar(500) | Sim |
| **MEMORIA_OCS** | Tamanho da memória detectada pelo OCS NG em megabytes | int | number(6,0) | Sim |

Tabelas referenciadas por HARDWARE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [LOCAL](dados_local) | \| **LOCAL** \| **HARDWARE** \| \|---\|---\| \| ID_LOCAL \| ID_LOCAL \| |
