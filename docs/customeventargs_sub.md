# Argumento

Caminho: Janelas > Utilitários > Classes de Negócio > Eventos Customização > Argumento

Argumentos disponibilizados pelo mecanismo invocador de Eventos Customizados. Estes argumentos, somente leitura, podem ser utilizados na implementação de regras de negócio contida no evento.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Nome** | Na implementação do script este argumento pode ser acessado por uma variável declarada com este Nome. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NAME da tabela [SV_CUSTOM_EVENT_ARGS](dados_sv_custom_event_args). |
|---|---|
| **Descrição** | Descrição detalhada sobre o conteúdo e utilização do argumento. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRIPTION da tabela [SV_CUSTOM_EVENT_ARGS](dados_sv_custom_event_args). |
| **Tipo** | Tipo de dados do argumento. No caso de classes de negócio o tipo se refere aquele disponível para o mecanismo de customização (proxies de customização). Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TYPE da tabela [SV_CUSTOM_EVENT_ARGS](dados_sv_custom_event_args). |
