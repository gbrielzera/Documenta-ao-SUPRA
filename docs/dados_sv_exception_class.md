# SV_EXCEPTION_CLASS

Caminho: Customização > Modelo de dados > Utilitários > SV_EXCEPTION_CLASS

Uma Exceção representa uma situação de erro verificada e documentada pelo sistema. Neste cadastro um usuário especial do sistema, denominado Administrador, pode customizar mensagens exibidas em situações de erro. Nesta customização é possível a utilização de propriedades na classe de negócio associada (veja o conteúdo da classe no Dicionário de Classes).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_EXCEPTION_CLASS** | Identificador da Exceção | int | number(6,0) | Não |
| **CODE** | Código identificador do erro. | varchar(50) | varchar(50) | Não |
| **MESSAGE** | Mensagem que é exibida para o usuário na ocorrência do erro. Esta mensagem pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | varchar(500) | varchar(500) | Não |
| **CAUSE** | Descritivo da Causa do Erro. Este descritivo pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | varchar(500) | varchar(500) | Não |
| **EFFECT** | Efeito que o Erro possa ter provocado no sistema. O descritivo do efeito pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | varchar(500) | varchar(500) | Não |
| **ACTION** | Orientação para o Usuário para resolução do problema. O descritivo da ação pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) | varchar(500) | varchar(500) | Não |
| **ORIGINAL_MESSAGE** | Conteúdo do campo Mensagem gerado pelo fabricante deste software e disponível para reversão de texto customizado. | varchar(500) | varchar(500) | Não |
| **ORIGINAL_CAUSE** | Conteúdo do campo Causa gerado pelo fabricante deste software e disponível para reversão de texto customizado. | varchar(500) | varchar(500) | Não |
| **ORIGINAL_EFFECT** | Conteúdo do campo Efeito gerado pelo fabricante deste software e disponível para reversão de texto customizado. | varchar(500) | varchar(500) | Não |
| **ORIGINAL_ACTION** | Conteúdo do campo Ação gerado pelo fabricante deste software e disponível para reversão de texto customizado. | varchar(500) | varchar(500) | Não |
| **ID_CLASS** | Identificador da Classe associada | int | number(6,0) | Não |

Tabelas referenciadas por SV_EXCEPTION_CLASS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_EXCEPTION_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_EXCEPTION_CLASS.*, SV_CLASS.NAME
from SV_EXCEPTION_CLASS, SV_CLASS
where SV_EXCEPTION_CLASS.ID_CLASS = SV_CLASS.ID_CLASS
```
