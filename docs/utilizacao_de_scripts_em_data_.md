# Formulários Dinâmicos

Caminho: Guia para Administradores > Configurando Processos > Tópicos Avançados > Formulários Dinâmicos

É possível realizar a criação de Formulários Dinâmicos, permitindo uma maior customização dos campos da Ordem de Serviço. Para isso, são utilizados scripts na linguagem IronPython. Além dos locais citados no tópico sobre [Tarefas](tarefas), também podem ser inseridos scripts a serem executados durante o preenchimento de campos.

A seguir, iremos explicar quais são os locais e as variáveis específicas disponíveis.

Script Formulário carregado Deve ser utilizado quando se deseja executá-lo apenas uma vez, ao início da tarefa corrente.

Localização do campo Script Formulário carregado

Neste script, estão disponíveis a seguintes variáveis:

- **Formulario -** possui as propriedades **Visivel**, **Habilitado** e **Valor**. Para campos do tipo Combobox, podemos alterar as opções através da propriedade **Itens**.

Script Modificado Utilizado em Entrada de Dados, deve-se utilizá-lo quando desejar executá-lo toda vez que ocorrer uma modificação no campo.

Localização do campo Script Modificado

Neste script, estão disponíveis a seguintes variáveis:

- **Formulario -** possui as propriedades **Visivel**, **Habilitado** e **Valor**. Para campos do tipo Combobox, podemos alterar as opções através da propriedade **Itens**.
- **Controle** - retorna o campo atual onde está sendo inserido o script, a qual possui as mesmas propriedades da variável **Formulario**.

## Scripts em Listagem de Registros

Para campos do tipo Listagem de Registros, podem ser inseridos scripts para serem executados em diferentes momentos, como durante a inserção, modificação ou exclusão de linhas.

### Script Adicionado

Executa o script ao clicar para adicionar uma nova linha. Para a criação deste script, temos as seguintes variáveis específicas:

- **Formulario -** possui as propriedades **Visivel**, **Habilitado** e **Valor**. Para campos do tipo Combobox, podemos alterar as opções através da propriedade **Itens**;
- **Tabela** - retorna um DataTable contendo os valores inseridos na listagem;
- **NovoRegistro** - retorna um HashTable que permite inicializar a nova linha com valores pré-definidos;
- **Posicao** - retorna a posição na listagem em que o novo registro está sendo adicionado.

### Script Confirmado

Executa o script ao clicar no botão de confirmação durante a criação ou edição de uma linha. Para a criação deste script, temos as seguintes variáveis específicas:

- **Formulario -** possui as propriedades **Visivel**, **Habilitado** e **Valor**. Para campos do tipo Combobox, podemos alterar as opções através da propriedade **Itens**;
- **Cancela** - se for definido como True cancela as modificações realizadas;
- **Registro -** retorna um HashTable contendo os valores atuais da linha em edição.

### Script Modificado

Executa o script ao editar uma linha. Para a criação deste script, temos as seguintes variáveis específicas:

- **Formulario -** possui as propriedades **Visivel**, **Habilitado** e **Valor**. Para campos do tipo Combobox, podemos alterar as opções através da propriedade **Itens**;
- **Controle** - retorna o campo atual onde está sendo inserido o script, a qual possui as mesmas propriedades da variável **Formulario**;
- **FormularioRegistro** - retorna um HashTable contendo os valores atuais da linha em edição.

### Script Removido

Executa o script ao clicar para remover uma linha existente na listagem. Para a criação deste script, temos as seguintes variáveis específicas:

- **Formulario -** possui as propriedades **Visivel**, **Habilitado** e **Valor**. Para campos do tipo Combobox, podemos alterar as opções através da propriedade **Itens**;
- **Tabela** - retorna um DataTable contendo os valores inseridos na listagem;
- **RegistroRemovido** - retorna um HashTable contendo os valores da linha a ser removida;
- **Posicao - **retorna a posição do registro que está sendo removido.
