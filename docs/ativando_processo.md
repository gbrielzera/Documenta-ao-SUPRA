# Ativar um Processo

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 1: Construindo o primeiro Processo > Ativar um Processo

Após concluir a edição de todos os fluxos de um processo é necessário ativar a versão em edição. Após a ativação o novo subprocesso estará disponível para usuários Solucionadores na tela Workspace e, dependendo da configuração, para usuários solicitantes no portal de Portal.

Antes de ativar a versão é interessante executar a rotina de Validação de versão, que identificará pendências no fluxo editado. Este comando está disponível na janela Process Explorer por meio do menu de contexto exibido quando selecionamos a versão ou subprocesso alvo. A mesma opção pode ser acionada pelo menu de contexto disponível no interior do diagrama conforme a figura abaixo:

Validação de uma versão

Validação de um subprocesso

Quando executamos a validação do nosso novo fluxo encontramos as seguintes mensagens:

Avisos relativos ao nosso fluxo

Como estas mensagens não são pendências vamos seguir no processo de ativação, que deve ser executada com o botão disponível na barra de ferramentas do Process Explorer ou no menu de contexto desta mesma janela.

**Importante: a operação de Ativação possui uma chamada implícita para a rotina de Validação, portanto não é possível ativar uma configuração inválida.**

Ativação de uma versão de Processo

Após acionar o comando de ativação será exibida uma mensagem de confirmação semelhante a figura abaixo. Clique em **Sim** para confirmar a ativação.

Configuração da ativação

Após a ativação a janela Process Explorer é atualizada exibido a versão 1 como a versão corrente (versão em produção neste momento):

Novo processo ativado no sistema

A partir deste momento já é possível abrir Ordens de Serviço na tela Workspace da aplicação Windows Supravizio ou no Portal (se o subprocesso estiver disponível para clientes via Portal de Processos).

Novo fluxo exibido no Workspace

Nosso novo subprocesso também aparece disponível na função de Abertura do Portal. Veja a figura abaixo:

Novo Subprocesso disponível
