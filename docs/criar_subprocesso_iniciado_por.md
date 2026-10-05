# Criar Subprocesso Iniciado por Email

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 12: Abertura de Ordem de Serviço por email > Criar Subprocesso Iniciado por Email

Para criação de um Subprocesso iniciado por e-mail, é necessário antes configurar uma caixa de e-mail com acesso POP3. Neste tutorial utilizaremos como exemplo o e-mail "tutorial14@supravizio.com"

Adicione no fluxo um Iniciador por Mensagem:

Iniciador por mensagem

Então nas propriedades do iniciador selecione o Tipo de Mensagem: "E-mail":

Tipo de Mensagem

Selecione <Nova..> em Caixa de E-mail:

Nova caixa de e-mail

Para configurar a caixa de e-mail preencha os campos, conforme a figura abaixo:

Nova Caixa de Mensagem

**Importante:** Para saber mais sobre a configuração de Caixas de Mensagem, leia o tópico [Configuração de Caixas de Mensagens](configuracao_de_caixas_de_mens).

Após confirmar a configuração da caixa, para testar se há conexão entre o Supravizio e a caixa de e-mail utilize a opção "Testar conectividade da caixa":

Testar conectividade

Caso a operação seja executada com sucesso o seguinte diálogo será exibido:

Conexão com sucesso

Para adicionar anexos do e-mail na Ordem de Serviço, preencha o campo "Anexar todos documentos" com "True" e indique o tipo de arquivo previsto a ser retornado:

Anexos

Como processos por e-mail não possuem nenhum indicador de "Serviço", é necessário pré definir qual o tipo de serviço que será realizado. Para isso, utilizamos a propriedade Serviço Inicial do iniciador automático. Neste caso, utilizamos o serviço "Serviços Administrativos".

Propriedade Serviço Inicial

A partir deste momento, todas as Ordens de Serviço deste tipo de subprocesso que forem iniciadas possuirão este Serviço.

Defina as demais atividades do fluxo do processo e ative:

Modelo de Fluxo

Observação: não esqueça de definir o responsável pelo iniciador por mensagem.
