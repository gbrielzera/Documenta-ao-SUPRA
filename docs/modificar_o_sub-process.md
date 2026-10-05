# Modificar o Subprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 3: Incluindo aprovações > Modificar o Subprocesso

Nesta etapa vamos introduzir o Data Object de aprovação e chegaremos ao seguinte resultado:

Resultado esperado ao término deste tópico

### 1. Selecione o Subprocesso da versão em edição utilizando o Process Explorer:

Seleção do novo fluxo

### 2. Selecione o fluxo que entra na atividade Realizar compra e clique na tecla Delete para remover a linha

Fluxo modificado

### 3. Na janela Toolbox selecione o elemento Tarefa e em seguida clique sobre o diagrama e complemente o descritivo conforme a figura:

Nova tarefa adicionada

### 4. Na janela Toolbox selecione a opção Aprovação:

Data Object de aprovação

### 5. Clique sobre a tarefa Solicitar aprovação do Presidente

Inclusão da aprovação

### 6. Na janela Toolbox selecione o botão Fluxo e adicione um fluxo entre o iniciador e a tarefa Solicitar aprovação do Presidente:

### Fluxo entre o iniciador e a aprovação

### 7. Selecione o Data Object de Aprovação e com o menu de contexto visualize a janela de Propriedades:

Janela de Propriedades para configuração da aprovação

### 8. Na janela de Propriedades da Aprovação clique no botão para adicionar aprovadores. No diálogo de aprovadores clique em Adicionar:

### Lista de papéis que definem as pessoas responsáveis pela aprovação

### 9. No aprovador adicionado selecione o valor <Novo...> no campo Aprovador conforme a figura abaixo:

### Criação de um papel utilizando o próprio editor

### 10. No novo diálogo de definição de papel preencha os seguintes dados, e após clique no botão em "Relação de pessoas e filas":

Novo Papel

11. Nesta nova janela, clique em "Adicionar" e após, no botão em "Pessoa/fila" para selecionar o usuário na lista de cadastros:

Relação de pessoas e filas que serão incluídas na recuperação

12. Na tela de busca, procure por "augusto" e selecione a opção "Augusto Magalhães", clicando em OK para incluí-lo:

Procurar Pessoa

13. Confirme as alterações até voltar a tela de Desenho de Fluxo.

14. Na aba "Propriedades", clique no botão em "Campos para Aprovação":

Inclusão de Campos para Aprovação

### 15. Novamente na janela Propriedades clique no botão da propriedade campos para aprovação e no diálogo de campos adicione dois campos conforme a figura:

### 16. Na janela Toolbox selecione o elemento Desvio Exclusivo:

### 17. Clique sobre o diagrama e complemente o rótulo conforme a figura abaixo:

### 18. Utilize o comando Link do Toolbox para adicionar um fluxo entre a tarefa de aprovação e o desvio e outro fluxo entre o desvio e a tarefa Realizar compra

Ligação entre a aprovação e a realização de compra

### 19. Utilizando o Toolbox selecione o elemento finalizador por Cancelamento:

Elemento Cancelamento do toolbox

### 20. Clique no diagrama e adicione um fluxo entre o desvio de aprovação e o novo finalizador por Cancelamento

### 21. Selecione a Atividade da aprovação e insira um Código:

Configuração do Campo "Código"

### 22. Selecione o desvio e selecione a aprovação na propriedade Regra de desvio:

### 23. No diagrama selecione a alternativa do desvio que atinge a tarefa Realizar compra e configure as propriedades Texto e Resultado da aprovação conforme a figura abaixo:

### 24. No diagrama selecione a alternativa do desvio que atinge o finalizador por Cancelamento e configure as propriedades Texto e Resultado da aprovação conforme a figura abaixo:

### 25. Por fim mude o responsável da atividade Realizar compra para o papel Comprador com menor carga

Mudança de responsabilidade para realizar compra
