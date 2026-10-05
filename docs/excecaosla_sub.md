# Exceção ANS

Caminho: Janelas > Recurso > Acordo de Nível de Serviço > Item de Acordo de Nível de Serviço > Exceção ANS

Redefinição do tempo de atendimento para períodos de exceção em um mês ou ano.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Período** | Tipo de Período de Exceção que pode ser um período compreendido em um Mês (dias de um mês para exceção) ou Ano (meses do ano para exceção). Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PERIODO da tabela [EXCECAO_SLA](dados_excecao_sla). |
|---|---|
| **Início** | Dia de início se o período for Mês ou mês de início se o período for Ano. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - O Início deve ser maior ou igual a 1 Este campo é mantido na coluna INICIO da tabela [EXCECAO_SLA](dados_excecao_sla). |
| **Fim** | Dia de fim se o período for Mês ou mês de fim se o período for Ano. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - O Fim deve ser maior ou igual a 1 Este campo é mantido na coluna FIM da tabela [EXCECAO_SLA](dados_excecao_sla). |
| **Tempo de atendimento (minutos)** | Tempo de atendimento (em minutos) para Ordens de Serviço enquadradas no critério de período de exceção. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TEMPO_ATEND da tabela [EXCECAO_SLA](dados_excecao_sla). |
