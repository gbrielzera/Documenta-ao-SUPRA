# APUR_IND_ITEM

Caminho: Customização > Modelo de dados > Processo > APUR_IND_ITEM

Apuração de Indicador de Desempenho que tenha como fonte de dados banco de Itens de Configuração.

Por se tratar de um tipo herdado de ApuracaoIndicador, a tabela APUR_IND_ITEM possui uma chave estrangeira apontando para a tabela [APURACAO_INDICADOR](dados_apuracao_indicador).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_INDICADOR** | Identificador do(a) Indicador associado(a) | int | number(6,0) | Não |
| **MES** | Mês | int | number(6,0) | Não |
| **ANO** | Ano | int | number(6,0) | Não |
| **SEQUENCIA** | Sequencia | int | number(6,0) | Não |
| **ID_PLANO_GESTAO** | Identificador do Plano de Gestão proprietário da apuração | int | number(6,0) | Não |
| **ID_ORGAO_CLIENTE** | Identificador do Orgao solicitante | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
