# Importação e Exportação de Fluxos de Processo

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Importação e Exportação de Fluxos de Processo

Através do Supravizio, é possível realizar a exportação de processos que foram criados em um determinado ambiente e importar em outro ambiente. Para que isso seja possível, é necessário que ambos os ambientes sejam da mesma versão.

Para realizar a exportação de um determinado processo (ou um Subprocesso, se necessário), basta acessar o **Editor de Processo**, selecionando o item de interesse. Por exemplo, vamos exportar o processo de **Incidentes** abaixo:

Process Explorer

Será exibida a seguinte mensagem no canto inferior esquerdo da tela do **Editor de Processos**:

Mensagem informando a geração do arquivo

Após gerada a exportação o Supravizio solicita que indique a pasta e nome de arquivo destino:

Tela de seleção do diretório

Para realizar a importação do processo exportado vá no destino e acesse o **Editor de Processos**. Caso não exista nenhuma versão ou processo similar, como neste exemplo, o processo de Incidentes, é necessário criar o processo. Para isso, no **Process Explorer**, clique na opção abaixo:

Novo Processo

Preencha as informações necessárias no cadastro do novo processo:

Informações do novo processo

Confirme e Feche o dialogo de cadastro e em seguida clique em Salvar no **Editor de Processos**. Repare no **Process Explorer** que foi criado o novo processo e já contendo uma nova versão **Em Edição**:

Versão inicial em edição

Caso deseje realizar a importação em um processo existente, basta selecioná-lo e clicar com o botão direito na opção **Nova Versão**:

Nova versão do processo existente

Clicando com o botão direito na versão **Em Edição** selecione a opção **Importar**:

Localização do comando Importar

Ao indicar o arquivo que foi exportado do outro ambiente, será exibida uma janela para que selecione quais os Subprocessos que serão importados:

Seleção de Subprocessos para Importação

É possível também realizara exportação/importação de Subprocessos isoladamente. Para isso, no ambiente em que irá exportar o processo basta selecionar o Subprocesso ao invés do processo e com o botão direito clicar em **Exportar**. Após isso, basta ir no ambiente destino e selecionar uma versão Em Edição do processo de interesse. Ao selecionar este comando será importado apenas Subprocesso necessário.

Após confirmar a importação dos Subprocessos necessários o Supravizio analisa todos os cadastros relacionados ao desenho do processo e exibe uma tela onde são informados os cadastros que serão criados, incluindo campos customizados e eventuais cadastros que serão alterados:

Pendências de Importação

Caso exista alguma mensagem de categoria **Erro** não será possível realizar a importação. Para confirmar a importação basta clicar no comando **Confirmar Importação**, caso contrário, clique em **Cancelar**.

Importando o processo, basta clicar no comando **Validar Versão** clicando com o botão direito na versão **Em Edição** do processo. Não existindo nenhuma pendência, basta **Ativar a versão**.

## Revisão de cadastros

O importador do Supravizio realiza a importação de novos cadastros, porém não modifica cadastros existentes, exceto o cadastro de campos customizados, caso identifique alguma mudança. Apenas os cadastros relacionados com a configuração dos fluxos dos processos são criados no ambiente destino nesta ação, como por exemplo, serviços disponíveis em tipos de Subprocesso, papéis, associações e modelos de comunicados.

É recomendado que seja feita a revisão dos principais cadastros relacionados com os processos que foram importados. Verificar cada um dos seus campos incluindo os seus registros associados através das abas dos cadastros. Esta tarefa pode ser feita após a importação dos processos.

Os principais cadastros que necessitam de revisão são:

### Do menu Processo | Processos:

- Associações
- Caixas de Mensagem
- Categorias
- Métodos de Priorização
- Modelos de Comunicado
- Tipos de Evento
- Tipos de Solicitação
- Tipos de Subprocesso
- Pesquisa de Satisfação | Grupos de Questões
- Pesquisa de Satisfação | Questões de Pesquisas
- Pesquisa de Satisfação | Classe de Pesquisa de Satisfação

### Do menu Processo | Serviços

- Classes de Serviços
- Grupos de Serviços
- Tipos de Serviços
- Serviços

### Do menu Recurso

- Grupos de Trabalho
- Calendários
- Acordos de Nível de Serviço | Motivos de Interrupção de ANS
- Acordos de Nível de Serviço | Acordos de Nível de Serviço

### Do menu Ativos

- Tipos de Itens de Configuração

## Campos customizados

É necessário também verificar nos formulários dos cadastros a inclusão de novos campos customizados. Para isso, basta selecionar um cadastro, por exemplo, o de Pessoas, selecionar um registro, abrir o formulário de cadastro e clicar no comando **Mais Campos**. Não é necessário entrar em todos os registros, apenas em um registro por cadastro. Caso não seja encontrado um determinado campo customizado no ambiente destino, comparando-o com o ambiente de origem da importação, basta cadastrar este novo campo no ambiente destino. Para isso leia o tópico [http://www.venki.com.br/help/supravizio/campos_customizados.htm](http://www.venki.com.br/help/supravizio/campos_customizados.htm)

Os cadastros mais comuns onde encontramos campos customizados são:

### Do menu Recurso:

Todos

### Do menu Ativos:

Todos exceto: Análise de Impacto e Importação de Hardware e Software

### Do menu Processo:

Todos de Processo | Serviço

## Scripts

Durante a importação, o sistema irá realizar a cópia dos scripts exatamente como foram criados. Muitas vezes, estes scripts utilizam dados que foram inseridos apenas no ambiente em que foi criado, como os citados acima (Cadastros e Campos Customizados).

Sendo assim, quando for exportado, o script pode não funcionar.

Neste caso, após o fluxo ser importado, a pessoa deverá renomear os campos no script (caso já existam, porém, com outro nome) ou alterar seus atributos manualmente.

**Importante**: A partir da versão 8.1.2, as [Bibliotecas de Script](biblioteca_de_scripts) que forem utilizadas no processo também serão exportadas com o mesmo. Portanto, caso já exista uma biblioteca com o mesmo nome no ambiente, esta será atualizada.
