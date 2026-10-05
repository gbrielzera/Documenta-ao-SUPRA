# RECURSO_APLICADO

Caminho: Customização > Modelo de dados > Recurso > RECURSO_APLICADO

Recurso a ser Aplicado no cumprimento do Contrato

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RECURSO_APLICADO** | Identificador do Recurso Aplicado | int | number(6,0) | Não |
| **ID_CONTRATO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | int | number(6,0) | Sim |
| **DESCRICAO** | Descrição completa do Recurso. Utilze descritivos de Função, Cargo ou Nome da Pessoa de forma a facilitar a referência na associação com Grupos de Trabalho. | varchar(500) | varchar(500) | Não |
| **VALOR_MENSAL** | Valor mensal | decimal(15,2) | number(15,2) | Sim |
| **VALOR_HORA** | Valor hora padrão para o recurso. O valor final pode variar em função do fator atribuiído ao tipo de apontamento realizado. | decimal(15,2) | number(15,2) | Sim |
| **QUANT_HORAS** | Quantidade de horas contratadas por mês. | int | number(6,0) | Sim |
| **VALIDA_SALDO** | Quantidade de meses para validade das horas que não forem utilizadas no mês apurado. Se não for preenchido ou for preenchido com o valor 0 significará que as horas devem ser consumidas no mesmo mês. Se for uma quantidade de meses igual ou superior ao restante de meses do contrato significará que as horas formarão um banco. | int | number(6,0) | Sim |
| **UTILIZA_ACUMULADOS_PRIM** | Utiliza créditos/débitos de saldos anteriores antes de utilizar o saldo de horas disponíveis para o mês. | char(3) | char(3) | Não |

Tabelas referenciadas por RECURSO_APLICADO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CONTRATO](dados_contrato) | \| **CONTRATO** \| **RECURSO_APLICADO** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| |

Tabelas que dependem de RECURSO_APLICADO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CONTRATO_TECNICO](dados_contrato_tecnico) | \| **CONTRATO_TECNICO** \| **RECURSO_APLICADO** \| \|---\|---\| \| ID_RECURSO_APLICADO \| ID_RECURSO_APLICADO \| |

**Exemplo 1: join com a tabela CONTRATO**

```
select RECURSO_APLICADO.*
from RECURSO_APLICADO, CONTRATO
where RECURSO_APLICADO.ID_CONTRATO = CONTRATO.ID_CONTRATO
```
