# TECNICO

Caminho: Customização > Modelo de dados > Recurso > TECNICO

Um Solucionador é uma Pessoa que trabalha no atendimento de solicitações de Serviço. Este solucionador deve estar lotado em somente um Grupo de Trabalho e pode exercer função de coordenação.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_TECNICO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tecnico | int | number(6,0) | Não |
| **ID_GRUPO_TRABALHO** | Identificador do Grupo de Trabalho | int | number(6,0) | Não |
| **ID_PESSOA** | Identificador da Pessoa associado | int | number(6,0) | Não |
| **ATIVO** | Indica que o Solucionador está Ativo no Grupo de Trabalho. Em um dado momento o Solucionador pode estar Ativo em somente um Grupo de Trabalho. Ele também não pode ser ativado em um Grupo de Trabalho desativado. | char(3) | char(3) | Não |
| **DATA_HORA_ASSOCIACAO** | Data e hora em que a Pessoa foi associada ao Grupo de Trabalho | datetime | date | Não |
| **DATA_HORA_DESATIVACAO** | Data e hora em que o Solucionador teve sua associação com o Grupo de Trabalho desativadda | datetime | date | Sim |
| **ALERTA_SOL_GRUPO** | Indica que Solucionadores do Grupo receberão alertas quando uma nova Ordem de Serviço for encaminhada para a fila. | char(3) | char(3) | Não |
| **ID_CALENDARIO** | Identificador do Calendário do recurso | int | number(6,0) | Sim |

Tabelas referenciadas por TECNICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **TECNICO** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [CALENDARIO](dados_calendario) | \| **CALENDARIO** \| **TECNICO** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **TECNICO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |

**Exemplo 1: join com a tabela PESSOA**

```
select TECNICO.*, PESSOA.NOME_ABREVIADO
from TECNICO, PESSOA
where TECNICO.ID_PESSOA = PESSOA.ID_PESSOA
```

**Exemplo 2: join com a tabela CALENDARIO**

```
select TECNICO.*, CALENDARIO.DESCRICAO
from TECNICO left outer join CALENDARIO on TECNICO.ID_CALENDARIO = CALENDARIO.ID_CALENDARIO
```

**Exemplo 3: join com a tabela GRUPO_TRABALHO**

```
select TECNICO.*
from TECNICO, GRUPO_TRABALHO
where TECNICO.ID_GRUPO_TRABALHO = GRUPO_TRABALHO.ID_GRUPO_TRABALHO
```
