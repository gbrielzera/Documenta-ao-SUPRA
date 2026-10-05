# Escopo Propriedades Customizada

Caminho: Janelas > Utilitários > Classes de Negócio > Propriedades Customizadas > Escopo Propriedades Customizada

Escopo para Propriedades Customizadas. Se não for cadastrada restrição de Escopo então a Propriedade Customizada vale para todos os objetos da Classe associada

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Propriedade** | Propriedade com tipo de dados primitivo (inteiro, string, data/hora etc) que será utilizada para filtro e definição do escopo. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
|---|---|
| **Operador** | Operador: igual, menor, maior que etc. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna OPERATOR da tabela [SV_CUSTOM_PROPERTY_SCOPE](dados_sv_custom_property_scope). |
| **Valor para comparação** | Valor da Propriedade para habilitar a Propriedade Customizada Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna VALUE_SCOPE da tabela [SV_CUSTOM_PROPERTY_SCOPE](dados_sv_custom_property_scope). |
