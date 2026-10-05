# Relatórios de Apoio Operacional

Caminho: Guia para Administradores > Editor de Relatórios > Publicando Relatórios > Relatórios de Apoio Operacional

Este tópico ensinará a como publicar um relatório no Assistente de Processos e no Portal de Processos de forma que possa servir como um relatório de apoio operacional. Este tem como pré-requisito a execução do tópico [Relatórios com Parâmetros](relatorios_com_parametros).

Observe o processo de Incidente do fluxo abaixo. Selecionamos uma atividade onde a tomada de decisões é muito frequente. Este é um caso típico de atividade onde pode ser necessário um relatório de apoio:

Vamos incluir então o relatório que criamos no tópico indicado no início deste tópico. Para isso, nas Propriedades da atividade selecionada vamos inserir o relatório:

Na janela de inserção de relatórios, clique em "Adicionar". Em seguida, na listagem "Relatórios" selecione o relatório "Relatório de Ordens de Serviço com Subprocesso".

Devemos agora parametrizar a consulta indicando que queremos listar inicialmente as Ordens de Serviço que sejam do fluxo de Incidente. Para isso, expanda a listagem Parâmetros e clique no símbolo (...).

Selecionando o parâmetro pSubprocesso, clique no símbolo (...) do campo Valor.

Insira o seguinte valor na janela de edição de script:

Salve as alterações no fluxo e abra uma nova Ordem de Serviço do tipo Incidente. Alcançando a atividade onde se encontra o relatório configurado, no Assistente de Processos aparecerá um novo comando para o solucionador:

Veja o relatório e repare que o parâmetro passado definiu que o Subprocesso fosse o próprio Subprocesso da OS, e repare também que ele pode ser modificado pois foi marcada a opção de Permitir Modificação no parâmetro como True:

### Publicando relatórios para consulta no Portal de Processos

Para utilizarmos um relatório de apoio operacional na página de consultas do Portal, faça as seguintes alterações.

Retorne ao Editor de Processos e selecione a atividade a qual inserimos o relatório de apoio. Expanda a propriedade Relatórios, expanda o relatório "Relatório de Ordens de Serviço Parametrizável" e marque a opção "Disponível na consulta do Portal" como **True** (verdadeiro).

Toda Ordem de Serviço deste processo que esteja nesta versão, exibirá o relatório na página de Consulta do Portal na seção "Atividades Executadas":

Ao clicar no link indicado, será exibida uma janela com o relatório considerando o parâmetro fornecido como filtro:
