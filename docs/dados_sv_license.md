# SV_LICENSE

Caminho: Customização > Modelo de dados > Utilitários > SV_LICENSE

Mantém dados de licenciamento do produto instalador.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_LICENSE** | Número sequencial gerado automaticamente pelo sistema para Identificar um License | int | number(6,0) | Não |
| **DATA** | Informações criptografadas sobre o licenciamento | text | clob | Sim |
| **OWNER** | Proprietário da licença de uso. | varchar(500) | varchar(500) | Não |
| **REGISTER_DATE** | Data em que foi realizada a importação do arquivo de licenciamento do produto. | datetime | date | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
