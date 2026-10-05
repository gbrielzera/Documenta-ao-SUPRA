# FIGURA

Caminho: Customização > Modelo de dados > Processo > FIGURA

Representa graficamente alguma ferramenta de modelagem BPMN - Business Processs Management Notation

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_FIGURA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Figura | int | number(6,0) | Não |
| **WIDTH** | Largura da figura | int | number(6,0) | Não |
| **HEIGHT** | Altura da figura | int | number(6,0) | Não |
| **TOP** | Posição em Y | int | number(6,0) | Não |
| **LEFT** | Posição em X | int | number(6,0) | Não |
| **ID_DIAGRAMA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Diagrama | int | number(6,0) | Não |
| **TIPO_GATEWAY** | Tipo de Gateway representado pela figura. | varchar(250) | varchar(250) | Sim |
| **TIPO_FIGURA_ATV** | Tipo de Figura associada com atividade de processo | varchar(250) | varchar(250) | Sim |
| **TIPO_EVENTO** | Tipo de evento (somente para Atividades do tipo Evento) | varchar(250) | varchar(250) | Sim |
| **ID_ATIVIDADE** | Identificador da Atividade associada com a Figura | int | number(6,0) | Sim |
| **ID_GATEWAY** | Identificador do Gateway associado a Figura | int | number(6,0) | Sim |
| **TIPO** | Tipo de Figura | varchar(250) | varchar(250) | Não |
| **ID_OPERACAO_ATIVIDADE** | Identificador de uma Operação Atividade se for um Data Object | int | number(6,0) | Sim |
| **TIPO_FIGURA_DO** | Tipo de Data Object representado pela figura. Data Objects são representações gráficas de Operações de Atividades. | varchar(250) | varchar(250) | Sim |
| **TEXTO** | Texto livre sobre a informação | varchar(500) | varchar(500) | Sim |
| **DATA_REQUERIDO_INCIAL** | Indica que o Data Object é requerido para início da Atividade (Entrada) | char(3) | char(3) | Não |
| **PRODUZIDO_TERMINO** | Indica que o Data Object é produzido ao término da Atividade (Saída) | char(3) | char(3) | Não |
| **DATA_ESTADO** | Indica a situação do Data Object antes ou após o processamento | varchar(50) | varchar(50) | Sim |
| **ID_CONTROLE** | Identificador do(a) Controle associado(a) | int | number(6,0) | Sim |
| **COMENT_VISIVEL_AA** | Indica que o comentário é visível nas páginas de abertura, consulta ou aprovação da aplicação de Autoatendimento. | char(3) | char(3) | Não |
| **LISTA_FLUXOS** | Lista de fluxos da figura | varbinary(4000) | blob | Sim |

Tabelas referenciadas por FIGURA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **FIGURA** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [GATEWAY](dados_gateway) | \| **GATEWAY** \| **FIGURA** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY \| |
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **FIGURA** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **FIGURA** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |
| [DIAGRAMA](dados_diagrama) | \| **DIAGRAMA** \| **FIGURA** \| \|---\|---\| \| ID_DIAGRAMA \| ID_DIAGRAMA \| |

Tabelas que dependem de FIGURA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FIGURA_ATIV_EVENTO_INTERM](dados_figura_ativ_evento_interm) | \| **FIGURA_ATIV_EVENTO_INTERM** \| **FIGURA** \| \|---\|---\| \| ID_FIGURA_EVENTO_INTER \| ID_FIGURA \| |
| [FIGURA_ATIV_EVENTO_INTERM](dados_figura_ativ_evento_interm) | \| **FIGURA_ATIV_EVENTO_INTERM** \| **FIGURA** \| \|---\|---\| \| ID_FIGURA \| ID_FIGURA \| |

**Exemplo 1: join com a tabela GATEWAY**

```
select FIGURA.*, GATEWAY.DESCRICAO
from FIGURA left outer join GATEWAY on FIGURA.ID_GATEWAY = GATEWAY.ID_GATEWAY
```

**Exemplo 2: join com a tabela CONTROLE**

```
select FIGURA.*, CONTROLE.DESCRICAO
from FIGURA left outer join CONTROLE on FIGURA.ID_CONTROLE = CONTROLE.ID_CONTROLE
```

**Exemplo 3: join com a tabela DIAGRAMA**

```
select FIGURA.*
from FIGURA, DIAGRAMA
where FIGURA.ID_DIAGRAMA = DIAGRAMA.ID_DIAGRAMA
```
