# DISPOSITIVO_TELEFONICO

Caminho: Customização > Modelo de dados > Ativos > DISPOSITIVO_TELEFONICO

Dispositivo Telefônico

Por se tratar de um tipo herdado de ItemConfiguracao, a tabela DISPOSITIVO_TELEFONICO possui uma chave estrangeira apontando para a tabela [ITEM](dados_item).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **NUMERO_LINHA** | Número de linha | varchar(50) | varchar(50) | Sim |
