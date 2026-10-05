# Criar um Subprocesso iniciado por Mensagem

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 13: Abertura de Ordem de Serviço por WebService > Criar um Subprocesso iniciado por Mensagem

Vamos criar um subprocesso capaz de ser iniciado através de um WebService.

Fluxo

No nosso exemplo utilizaremos um subprocesso denominado "Problema". Adicione um iniciador por mensagem, clique em Propriedades e configure conforme a figura:

**Configuração mensagem WebService**

O Tipo de Mensagem deve ser configurado para WebService e deve ser definido um responsável. O Nome da mensagem é um identificador para diferenciar mensagens enviadas ao WebService de diferentes Ordens de Serviço. No exemplo o Nome da mensagem será definido "Reclamacao".

Como o nosso WebService irá enviar dois parâmetros, eles devem ser configurados em "Script Evento" com o seguinte código:

OrdemServico.DescricaoDetalhada = Parametros["DESC"]

OrdemServico.Assunto = Parametros["ASSUNTO"]

**Script Evento**

Neste caso de exemplo são enviados dois parâmetros: Descrição e Assunto.

Configure o fluxo conforme a figura abaixo:

**Fluxo**
