# ARTEFATO

Caminho: Customização > Modelo de dados > Ativos > ARTEFATO

Itens de Configuração do tipo 'Artefato'. Um Artefato é o produto de uma fase qualquer do ciclo de desenvolvimento de um software. Exemplos: código fonte, modelo ER, especificação funcional etc

Por se tratar de um tipo herdado de ItemConfiguracao, a tabela ARTEFATO possui uma chave estrangeira apontando para a tabela [ITEM](dados_item).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
