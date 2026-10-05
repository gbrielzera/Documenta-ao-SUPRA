# SOFTWARE

Caminho: Customização > Modelo de dados > Ativos > SOFTWARE

Itens de Configuração do tipo 'Licenças de Software'.

Por se tratar de um tipo herdado de ItemConfiguracao, a tabela SOFTWARE possui uma chave estrangeira apontando para a tabela [ITEM](dados_item).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **VERSAO** | Versão do Software | varchar(50) | varchar(50) | Sim |
| **REFERENCIA_LICENCA** | Dados de referência para o Licenciamento do Software | varchar(500) | varchar(500) | Sim |
| **COPIAS_LIC** | Número de cópias licenciadas | int | number(6,0) | Sim |
| **INST_AUDIT** | Instalações auditadas | int | number(6,0) | Sim |
