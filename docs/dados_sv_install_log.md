# SV_INSTALL_LOG

Caminho: Customização > Modelo de dados > Utilitários > SV_INSTALL_LOG

Mensagens geradas pelas rotinas de instalação. Este log é consultado por uma janela exibida após configuração da camada servidora.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ROUTINE** | Nome de identificação da rotina executada durante atualização do software | varchar(100) | varchar(100) | Não |
| **MESSAGE** | Mensagem gerada pela rotina de atualização. | varchar(500) | varchar(500) | Não |
| **STATUS** | Situação corrente do processamento indicando que: ainda está em execução, foi finalizado com sucesso ou foi finalizado com erros. | varchar(50) | varchar(50) | Não |
| **DATE_TIME** | Data e hora de registro da mensagem | datetime | date | Não |
