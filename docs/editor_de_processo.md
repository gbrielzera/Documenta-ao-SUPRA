# Editor de Processos

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos

A configuração de Processos do Supravizio é feita com uso da ferramenta **Editor de Processos. **O **Editor de Processos** possui interface gráfica para modelagem de fluxos seguindo uma notação de mercado denominada BPMN (Business Process Modeling Notation).

Todos os fluxos modelados no **Editor de Processos** ficam disponíveis para a equipe de Solucionadores (usuários que atendem solicitações) e para Clientes que utilizam o Portal de Processos. Durante a modelagem do fluxo o Analista de Processos configura regras de negócio no fluxo que são utilizadas pela Máquina de Processos para determinar o comportamento das ocorrências de um processos, denominadas como Ordens de Serviço.

Para acessar o **Editor de Processos** utilize as opções do menu Processo | Processos | Editor de Processos de acordo com a imagem abaixo:

Acesso ao Editor de Processos

Após o **Editor de Processos** conforme a figura acima será exibida a tela desta ferramenta que possibilita a configuração de Processos:

Observando a tela acima, podemos identificar do lado esquerdo janela** [Toolbox](toolbox)**. Esta janela disponibiliza as ferramentas BPMN necessárias para modelagem dos fluxos dos Processos.

Janela Toolbox

Ao lado direito podemos observar a janela do** [Process Explorer](process_explorer),** que é utilizada para acessar todos os macro-processos, processos e subprocessos, inclusive de versões desatualizadas.

Janela Process Explorer

Também ao lado direito da janela acima, fica disponível uma aba para acesso da a janela de** [Propriedades](propriedades_editor)** que exibe os atributos e scripts Python do(s) elemento(s) selecionado(s) no editor.

Janela de Propriedades

Na parte superior da tela do Editor de Processos existe uma barra de ferramentas com os principais comandos da janela:

Barra de ferramentas

Veja na tabela abaixo a relação completa de botões desta barra:

| **Botão** | **Descrição** |
|---|---|
|  | Ao clicar neste botão serão salvas todas as modificações de todos os Processos modificados na edição corrente. |
|  | O botão de editar traz as seguintes opções: Desfazer ou atalho Ctrl +Z, Refazer ou o atalho Ctrl + Y, Copiar ou o atalho Ctrl + C, Colar ou o atalho Ctrl + V, Recortar ou o atalho Ctrl + X e Selecionar tudo ou o atalho Ctrl + A. |
|  | Com este botão é possível remover todos um objeto selecionado no editor de processos. |
|  | Define o nível de Zoom na visualização do fluxo selecionado. |
|  | Alinha os objetos selecionados no diagrama de fluxo para o topo do diagrama considerando as coordenadas do primeiro objeto selecionado. |
|  | Alinha os objetos selecionados no diagrama de fluxo para a esquerda do diagrama considerando as coordenadas do primeiro objeto selecionado. |
|  | Centraliza os objetos selecionados ao eixo vertical. |
|  | Centraliza os objetos selecionados ao eixo horizontal considerando as coordenadas do primeiro objeto selecionado. |
|  | Deixa o espaçamento igual na vertical dos objetos selecionados considerando as coordenadas do primeiro objeto selecionado. |
|  | Deixa o espaçamento igual na horizontal dos objetos selecionados. |
|  | Exibe o diálogo de edição de campos customizados. |

Comandos da Barra de Ferramentas

## Manutenção de Campos customizados

Utilizando o comando Definição de Campos da tabela anterior podemos dar manutenção nos campos customizados do tipo de dado Venki.Supravizio.Processo.OrdemServico.

A figura abaixo ilustra este diálogo que lista todos os campos customizados que podemos incluir nos processos. Para acessar este diálogo utilize o comando **Mais Ações | Definição de campos** disponível na barra de ferramentas do editor de processos.

Diálogo para manutenção de campos customizados
