# SV_GLOBAL

Caminho: Customização > Modelo de dados > Utilitários > SV_GLOBAL

Informações globais sobre a instalação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GLOBAL** | Número sequencial gerado automaticamente pelo sistema para Identificar um Global | int | number(6,0) | Não |
| **APP_VERSION** | Versão da aplicação | varchar(500) | varchar(500) | Não |
| **STATUS** | Situação final após atualização de versão | varchar(100) | varchar(100) | Sim |
| **STATUS_MESSAGE** | Mensagem para esclarecimento sobre a situação. Se a situação for Erro, por exemplo, esta mensagem contém a mensage de Exceção. | varchar(500) | varchar(500) | Sim |
