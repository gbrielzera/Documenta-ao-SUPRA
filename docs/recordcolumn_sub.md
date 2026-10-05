# Campos de registros

Caminho: Janelas > Utilitários > Classes de Negócio > Propriedades Customizadas > Campos de registros

Campos de registros utilizados em propriedades customizadas do tipo Listagem de registros

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Nome** | Nome da coluna do registro. No caso de campos persistentes este nome é utilizado para criar uma coluna na tabela onde são persistidos os registros. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo Este campo é mantido na coluna NAME da tabela [SV_REC_COLUMN](dados_sv_rec_column). |
|---|---|
| **Descrição resumida** | Descrição resumida que é exibida no rótulo de controles utilizados na edição da coluna. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TEXT da tabela [SV_REC_COLUMN](dados_sv_rec_column). |
| **Tipo** | Tipo de dado da coluna Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TYPE da tabela [SV_REC_COLUMN](dados_sv_rec_column). |
| **Quantidade caracteres** | Tamanho de campos string em quantidade de caracteres. Se não for preenchido então é adotado o tamanho padrão de 250 caracteres |
| **Fórmula de cálculo** | Fórmula utilizada para cálculo de campos. Campos calculado não são persistidos em banco de dados. |
| **Ordem de exibição** | Sequencial para apresentação no controle grid utilizado para visualização e edição Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SEQUENCE da tabela [SV_REC_COLUMN](dados_sv_rec_column). |
| **Controle** | Controle utilizado para edição da coluna do registro Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CONTROL da tabela [SV_REC_COLUMN](dados_sv_rec_column). |
| **Largura** | Largura do controle utilizado para Edição da coluna. Quando não definido o sistema assume valor default conforme controle selecionado. |
| **Listagem de itens** | Listagem de itens disponíveis para seleção em um controle do tipo combobox. |
| **Script para recuperação de opções** | Script utilizado para recuperação de itens utilizados como opções de preenchimento para o campo. Para o caso específico de recuperação a partir de banco de dados, se for fornecida uma tabela com dois campos então o primeiro será utilizado para preenchimento do campo enquanto o segundo fornecerá as opções exibidas no controle. |
