# EVENTO_OCORR

Caminho: Customização > Modelo de dados > Processo > EVENTO_OCORR

Um Evento é um fato ocorridos durante o ciclo de vida de uma Ocorrência de Processo. Um evento pode ser utilizado para envio de um comunicado. Esta função pode ser configurada no cadastro do Tipo de Evento associado.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **DATA_HORA_EVENTO** | Data e hora de ocorrência do Evento | datetime | date | Não |
| **ID_TIPO_EVENTO** | Identificador do Tipo de Evento associado | int | number(6,0) | Não |
| **ID_RESPONSAVEL** | Identificador do Solucionador responsável associado ao Evento. | int | number(6,0) | Não |
| **ID_OCORRENCIA** | Identificador da Ocorrência proprietária do Evento | int | number(6,0) | Não |
| **MENSAGEM** | Mensagem detalhada do evento. A mensagem pode ser configurada por fórmula no Tipo de Evento associado. | varchar(500) | varchar(500) | Não |
| **DISP_AA** | Indica que o evento está disponível na página de consultas do Autoatendimento | char(3) | char(3) | Não |
| **PERM_CANC_PUB_AA** | Permite o cancelamento da publicação no Autoatendimento da resposta informada pelo solucionador. Caso não seja permitido cancelar, apenas os superiores do solucionador poderão cancelar a publicação (independente desse parâmetro). | char(3) | char(3) | Não |
| **NOME_AUTOR** | Nome da pessoa responsável pela geração do evento. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por EVENTO_OCORR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIPO_EVENTO](dados_tipo_evento) | \| **TIPO_EVENTO** \| **EVENTO_OCORR** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **EVENTO_OCORR** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **EVENTO_OCORR** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela TIPO_EVENTO**

```
select EVENTO_OCORR.*, TIPO_EVENTO.NOME
from EVENTO_OCORR, TIPO_EVENTO
where EVENTO_OCORR.ID_TIPO_EVENTO = TIPO_EVENTO.ID_TIPO_EVENTO
```

**Exemplo 2: join com a tabela OCORRENCIA**

```
select EVENTO_OCORR.*
from EVENTO_OCORR, OCORRENCIA
where EVENTO_OCORR.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```
