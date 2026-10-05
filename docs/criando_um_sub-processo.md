# Criar um Subprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 1: Construindo o primeiro Processo > Criar um Subprocesso

O **Subprocesso** é a entidade que utilizamos para desenhar um fluxo, composto de eventos, tarefas e decisões. Um **Subprocesso** está contido em um** Processo** e pode interfacear com diversos outros **Subprocessos**.

O Processo, por sua vez, está contido dentro de um Macroprocesso. Vamos ilustrar com o exemplo utilizado neste tutorial.

Hierarquia de Processos

Para criar um novo Subprocesso selecione a versão em edição do [novo Processo](criando_um_processo), clique com o botão direito do mouse para acessar o menu de contexto do [Process Explorer](process_explorer) e em seguida selecione a opção **Adicionar novo Subprocesso** conforme a figura abaixo:

Criação de novo Subprocesso

Ao executarmos o comando acima será apresentada a tela abaixo, onde iniciaremos o cadastro do novo Subprocesso:

Cadastro de Tipo de Subprocesso

Todos os campos deste cadastro representam características que não variam entre as diversas versões que este fluxo acumulará no decorrer do tempo. O campo **Descrição** é exibido em diversas janelas da aplicação Supravizio enquanto **Descritivo cliente** é apresentado na aplicação do Portal.

O campo **Nome abreviado **permite referenciar o Subprocesso em scripts Python que são úteis para automatizar um determinado fluxo.

O campo **Documentação** é incluído na documentação gerada pela própria ferramenta.

A opção **Ativo** indica que é possível gerar solicitações deste fluxo. Quando inativo o subprocesso será apresentado na janela Process Explorer em um item com fundo de cor amarela.

O** [Método de Priorização](metodopriorizacao_sub)**, define a metodologia para priorização de ocorrências e cálculo de ANS que será utilizada entre as cadastradas para este Subprocesso (não precisa ser preenchido).

A opção **Disponível para consulta como Base de Conhecimento** permite que Ordens de Serviço do subprocesso sejam recuperadas pela consulta de base de Conhecimento quando for selecionada a opção **Incluir dados de Ordens de Serviço**.

Recuperação de Ordens de Serviço como Base de Conhecimento

A opção **Habilita consulta automática de Base de Conhecimento** ativa uma busca automática na tela de edição de Ordem de Serviço a partir dos artigos da base de conhecimento utilizando como critério os campos nativos Descrição detalhada, Assunto e Sintoma analisado. Se existirem artigos encontrados nesta busca então o botão **Conhecimento** ganhará um fundo verde.

Busca automática na base de conhecimento

Em **Regra de visualização de Ordens de Serviço** é possível escolher uma regra de autorização para visualização de Ordens de Serviço do subprocesso. Se este campo não for preenchido o sistema utilizará o parâmetro default cadastro na tela de Configurações.

Em **Acesso total para usuários com perfil Administradores **é possível indicar que usuários com perfil Administrador possuam acesso total em ocorrências do subprocesso, independente da regra de visualização.

O **Órgão proprietário** é o órgão responsável pela execução do subprocesso.

O **Fator Prioridade** pode ser utilizado em algum método de priorização para calcular automaticamente a prioridade de Ordens de Serviço do subprocesso.

Os campos **Valor Charge-back** e **Critério Charge-back** estão relacionados com a cobrança pelo serviço prestado pelo Subprocesso que é realizado pelo módulo de Charge-back.

Opções de comunicados no cadastro de Subprocesso

No campo **Emails para cópia em comunicado manual**, pode se preencher uma relação de emails (separados por ; ou ,) para que em todos comunicados manuais daquele subprocesso seja enviada cópias do comunicado para os emails listados.

Os campos **Nome do remetente em comunicado manual** e **E-mail do remetente em comunicado manual**, podem ser redefinidos o nome e e-mail do remetente utilizados para comunicados enviados através da [aba Comunicados](comunicados) nas telas de Edição de Ordem de Serviço.

Cadastro de Tipo de Subprocesso - Portal

A opção **Permitir reabertura** pode ser utilizado em conjunto com o parâmetro** [Máximo dias para reabertura](configuracoes_autoatendimento)** para permitir que o cliente faça a reabertura de uma Ordem de Serviço utilizando as páginas de Consulta e Pesquisa de Satisfação do Portal. O cliente pode reabrir através do Portal se o campo** Permitir reabertura** estiver marcado, se a quantidade de dias corridos desde a finalização for menor ou igual ao parâmetro **Máximo dias para reabertura** e se a Ordem de Serviço não foi gerada por outro processo.

O campo **Visibilidade** define regras de visibilidade na consulta de Ordens de Serviço disponível no Portal de Processos. Utilizando esta configuração podemos tornar Ordens de Serviço públicas para todos os usuários, para pessoas lotadas no mesmo órgão ou empresa.

A **Publicação de Apontamentos** define as regras para publicar um apontamento (Permitir publicação mas como padrão não publicar, Permitir publicação e com padrão publicar, Nunca publicar ou Sempre publicar) .

A **Ordem de Exibição** indica a posição do Subprocesso no passo 2 da tela de abertura de Ordens de Serviço. Todos os Subprocessos que possuem este campo preenchido possuem prioridade de exibição e listadas de acordo com a posição indicada. Veja o exemplo abaixo:

Ordenação de Subprocessos

Importante: Para que esta regra seja atendida, é necessário que nas configurações do módulo de Abertura do Portal esteja habilitada a opção Destacar Subprocessos com Ordem de Exibição, conforme este [tópico](portal_abertura_configuracao_assist).

Preencha o formulário conforme a figura Cadastro de um Tipo de Subprocesso e depois clique em **Confirmar**. Finalizado o cadastro, é apresentado o diagrama do fluxo onde podemos adicionar eventos, tarefas e decisões:

Diagrama em branco relativo ao novo Subprocesso

A partir de agora iniciaremos a construção do fluxo conforme o tópico [Criar Fluxos de Processos](criando_fluxos_de_processos).
