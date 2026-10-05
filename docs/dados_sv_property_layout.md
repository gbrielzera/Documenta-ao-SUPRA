# SV_PROPERTY_LAYOUT

Caminho: Customização > Modelo de dados > Utilitários > SV_PROPERTY_LAYOUT

Layout de Classes e Propriedades

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PROPERTY_LAYOUT** | Identificador do Layout | int | number(6,0) | Não |
| **ID_PROPERTY** | Identificador da Propriedade | int | number(6,0) | Não |
| **GROUP_NAME** | Nome do Agrupamento. Se não for preenchido considerar como Grupo Principal | varchar(500) | varchar(500) | Sim |
| **GROUP_SEQUENCE** | Sequencial do Grupo no formulário. Se Group não for preenchido considerar o valor default -1 | int | number(6,0) | Não |
| **SEQUENCE** | Sequencial do Controle dentro do seu agrupamento | int | number(6,0) | Não |
| **WIDTH** | Largura em pixels do Controle | int | number(6,0) | Não |
| **HEIGHT** | Altura em pixels do Controle | int | number(6,0) | Não |
| **CONTROL** | Controle para edição da Propriedade | varchar(250) | varchar(250) | Não |
| **CONTROL_URL** | Caminho para carga do Controle em caso de Controles do tipo CustomControl | varchar(500) | varchar(500) | Sim |
| **VISIBLE** | Indica que o Controle está visível | char(3) | char(3) | Não |
| **ENABLED** | Indica que o Controle está ativo | char(3) | char(3) | Não |
| **CONTROL_CABABILITIES** | Recursos disponíveis para o Controle. Exemplos: UpperCase para controles TextBox. O recurso é variável de acordo com o Controle. | varchar(500) | varchar(500) | Sim |
| **GROUP_PARENT** | Nome do agrupamento Pai | varchar(500) | varchar(500) | Sim |
| **GROUP_CONTROL** | Tipo de controle utilizado como container do agrupamento. Se não for especificado considerar container default para a interface. | varchar(250) | varchar(250) | Não |
| **FORM_ID** | Identificador do tipo de Formulário | int | number(6,0) | Não |
| **ID_CLASS** | Identificador da Classe de uso apenas para otimização de carga | int | number(6,0) | Não |

Tabelas referenciadas por SV_PROPERTY_LAYOUT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **SV_PROPERTY_LAYOUT** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |

**Exemplo 1: join com a tabela SV_PROPERTY**

```
select SV_PROPERTY_LAYOUT.*, SV_PROPERTY.NAME
from SV_PROPERTY_LAYOUT, SV_PROPERTY
where SV_PROPERTY_LAYOUT.ID_PROPERTY = SV_PROPERTY.ID_PROPERTY
```
