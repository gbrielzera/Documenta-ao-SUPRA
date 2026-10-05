# Remoção de Ordens de Serviço em Qualidade

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Remoção de Ordens de Serviço em Qualidade

No momento que estamos modelando o processo, em qualidade, é comum realizar várias mudanças no fluxo, sendo cada uma delas testadas abrindo algumas Ordens de Serviços. Para que não necessitemos gerar uma versão do processo para cada mudança, geralmente realizamos a mudança na versão corrente e salvamos.

Ao tentar apagar uma Ordem de Serviço, pode ocorrer de aquela OS esteja relacionada, ou algo esteja relacionado a mesma, impedindo a exclusão.

Para que isso não ocorra, deve ser feita a exclusão através do comando encontrado no editor de processos, clicando com o botão direito do mouse no processo | Mais ações | Apagar Ordens de Serviço...

**Importante: A Remoção de Ordens de Serviço só é possível em [Ambiente de Qualidade](ambiente_de_qualidade).**

Apagar Ordens de Serviço

Ao clicar abrirá a seguinte tela:

Selecionando Ordens de Serviço para exclusão

Podemos selecionar quantas Ordens de Serviço forem necessárias, para isso segure a tecla Ctrl para selecionar uma ou mais Ordens de Serviço, Ctrl + Shift para selecionar um intervalo e para selecionar todas utilizamos o Ctrl + A.

Ao clicar em OK, serão excluídas as Ordens de Serviço. Elas são removidas do banco de dados diretamente, e não será feita a reciclagem do número das Ordens de Serviços.

Excluindo Ordens de Serviço
