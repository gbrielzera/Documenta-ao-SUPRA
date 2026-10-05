# AUSENCIA

Caminho: Customização > Modelo de dados > Recurso > AUSENCIA

Registra a Ausência Temporária de um Solucionador. Com este registro o sistema impoem restrições em algumas operações como o Encaminhamento.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_AUSENCIA** | Identificador da Ausência | int | number(6,0) | Não |
| **MOTIVO** | Motivo para a ausência | varchar(500) | varchar(500) | Não |
| **DATA_HORA_INICIO** | Data e hora de início de validade para a regra de Ausência Temporária | datetime | date | Não |
| **DATA_HORA_PREV_RETORNO** | Data e hora para Previsão de retorno do Solucionador | datetime | date | Não |
| **DATA_HORA_REGISTRO** | Data e hora de registro da Ausência Temporária | datetime | date | Não |
| **ID_SUBSTITUTO** | Identificador da Pessoa associada | int | number(6,0) | Não |
| **ID_PESSOA** | Identificador da Pessoa para qual foi registrado o período de Ausencia | int | number(6,0) | Não |
| **PERM_SUBS_MOD** | Permitir que o Substituto modifique todas as Ordens de Serviço no período de ausência | char(3) | char(3) | Não |
| **ENC_SUBSTITUTO** | Redirecionar encaminhamentos para o Substituto | char(3) | char(3) | Não |

Tabelas referenciadas por AUSENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **AUSENCIA** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **AUSENCIA** \| \|---\|---\| \| ID_PESSOA \| ID_SUBSTITUTO \| |

**Exemplo 1: join com a tabela PESSOA**

```
select AUSENCIA.*, PESSOA.NOME_ABREVIADO
from AUSENCIA, PESSOA
where AUSENCIA.ID_PESSOA = PESSOA.ID_PESSOA
```

**Exemplo 2: join com a tabela PESSOA**

```
select AUSENCIA.*, PESSOA.NOME_ABREVIADO
from AUSENCIA, PESSOA
where AUSENCIA.ID_SUBSTITUTO = PESSOA.ID_PESSOA
```
