# SV_CULTURE

Caminho: Customização > Modelo de dados > Utilitários > SV_CULTURE

Cultura disponível para localização de conteúdo de objetos de negócio. Todo usuário possui uma cultura associada e esta cultura é importante para apresentação da interface que pode ser localizada.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CULTURE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Cultura | int | number(6,0) | Não |
| **DESCRIPTION** | Descrição detalhada do Culture | varchar(500) | varchar(500) | Não |
| **SHORT_NAME** | Nome resumido que identifica uma Cultura na tecnologia Microsoft.NET | varchar(50) | varchar(50) | Não |

Tabelas que dependem de SV_CULTURE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_LOCALIZATION](dados_sv_localization) | \| **SV_LOCALIZATION** \| **SV_CULTURE** \| \|---\|---\| \| ID_CULTURE \| ID_CULTURE \| |
