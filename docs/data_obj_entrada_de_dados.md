# Entrada de Dados

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Data Objects > Entrada de Dados

Um Data Object do tipo Entrada de Dados define regras de preenchimento de campos de uma Ordem de Serviço. Estes campos podem ser nativos ou customizados pelo administrador do sistema.

Para adicionar um elemento deste tipo basta selecionar o item **Entrada de Dados** no Toolbox e em seguida clicar sobre uma Tarefa, Evento Iniciador ou Evento Finalizador contido no diagrama. Após adicionar o item selecione a janela de propriedades e clique no botão que aciona o diálogo de configuração da coleção **Campos para Preenchimento** (veja figura abaixo).

Exemplo de Data Object do tipo Entrada de Dados

Ao clicar no botão da propriedade **Campos para Preenchimento** é apresentado o diálogo onde podemos relacionar os campos que serão preenchidos. Os campos definidos no atributo **Nome** podem ser nativos (já presentes na tabela de Ordens de Serviço) ou customizado (criado pelo próprio usuário). Veja a figura abaixo:

Configurando os campos da Entrada de Dados

Ao definir uma regra de preenchimento de campo este é sempre exibido no Assistente de Processo quando o usuário estiver na atividade que detém a regra. Veja a figura abaixo que ilustra o preenchimento de campo para o fluxo visualizado anteriormente:

Preenchimento de campos no Assistente de Processos

A configuração de preenchimento de campo também tem efeito em iniciadores manuais de fluxos disponíveis no Portal. Neste caso o preenchimento de campo é realizado no quarto passo do assistente de abertura de Ordem de Serviço. Veja a figura abaixo considerando o mesmo fluxo acima:

Preenchimento de campos na abertura do Portal de Processos

Nas duas figuras acima observe que o preenchimento é obrigatório que foi configurado utilizando o atributo **Tipo de preenchimento** igual a **Obrigatório**. Este atributo ainda pode assumir os valores **Opcional** e **Opcional recomendado**. Esta última opção exibe uma mensagem de aviso quando a Ordem de Serviço é validada e **não** caracteriza uma pendência de processo.

**Importante:** No tópico [Criação de Campos Customizados](criacao_de_campos_customizados), explicamos sobre a criação de novos campos e customização dos mesmos.

Após o preenchimento, o conteúdo destes campos estarão presentes na aba Dados Principais na tela de [Edição de Ordem de Serviço](editar_ordemservico):

O campo Descrição detalhada na tela de edição de Ordem de Serviço

**Importante:** Em alguns casos, pode ser necessário que alguns campos não estejam disponíveis para edição ou fiquem desabilitados. Para isso, podemos desabilitar por script estes campos, como no exemplo seguinte, onde inserimos um script para desabilitar campos e alterar a visibilidade de outro.

Script inserido

Assim, ao passar pelo fim da atividade, os campos Nome e Sobrenome estarão desabilitados e note também que o campo Fornecedor não está mais visível:

Campos preenchidos

### Organização do layout de campos

É possível organizar a exibição dos campos para preenchimento em colunas. Para isso, basta alterar a propriedade **Coluna** na configuração do campo:

Propriedade Coluna

Ao exibir o formulário, os campos estarão divididos em suas respectivas colunas definidas na configuração, conforme o exemplo abaixo:

Campos divididos em colunas

### Particularidades do campo Favorecido

O campo **Favorecido** possui algumas particularidades, como a opção **Permite vários favorecidos na abertura pelo portal**.

Configurações do campo

Habilitando esta opção será possível selecionar mais de um Favorecido para a Ordem de Serviço:

Campo no Portal de Processos

Selecionando mais de um Favorecido, serão abertas Ordens de Serviço individualmente para cada um destes selecionados.
