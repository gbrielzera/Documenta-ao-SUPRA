# Eventos Customização

Caminho: Janelas > Utilitários > Classes de Negócio > Eventos Customização

Evento para disponível para Customização em uma determinada Classe de Negócio. Todos os eventos são implementados pela linguagem de scripts Python e podem acessar propriedades da Classe de Negócio customizada.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Nome** | Nome do Evento Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NAME da tabela [SV_CUSTOM_EVENT](dados_sv_custom_event). |
|---|---|
| **Descrição** | Descrição detalhada sobre quando o Evento é disparado pelo sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRIPTION da tabela [SV_CUSTOM_EVENT](dados_sv_custom_event). |

| **Implementações** | Implementações do Evento. Cada implementação está associada a um Domínio. Todos os registros desta coleção de dados são mantidos na tabela [SV_CUSTOM_EVENT_IMPL](dados_sv_custom_event_impl). |
|---|---|

| **Argumentos** | Parâmetros fornecidos pelo mecanismo de invocação de eventos. Estes argumentos, somente leitura, podem ser utilizados para customização de regras de negócio em classes do sistema. Todos os registros desta coleção de dados são mantidos na tabela [SV_CUSTOM_EVENT_ARGS](dados_sv_custom_event_args). |
|---|---|
