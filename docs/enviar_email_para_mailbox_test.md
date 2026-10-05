# Enviar Email para mailbox teste

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 12: Abertura de Ordem de Serviço por email > Enviar Email para mailbox teste

Para este tutorial utilizamos o mailbox tutorial14@supravizio.com que foi configurado no [Criar Subprocesso Iniciado por Email](criar_subprocesso_iniciado_por).

Inicialmente, é necessário determinarmos o cliente da Ordem de Serviço que será aberta através de um mailbox. Para determinarmos isso, é necessário que o email do remetente esteja cadastrado em algum dos registros do cadastro de Pessoas do Supravizio (Recurso | Pessoas).

**Pessoas**

Por exemplo modificando o usuário "José Oliveira" para ser o nosso remetente:

**Editar Pessoa**

Modifique na aba Dados para Contato o Email:

**Editar Email**

Salve as alterações e agora podemos enviar nosso email através do "teste01@supravizio.com" que o sistema reconhecerá José Oliveira como cliente da Ordem de Serviço.

**IMPORTANTE**: Caso o email do remetente não esteja cadastrado em nenhum registro do cadastro de Pessoas, então o cliente da Ordem de Serviço será o Sistema.

Na criação do novo email repare que o destinatário deve ser o mesmo configurado no tópico anterior (tutorial14@supravizio.com). O Assunto do email será o Assunto da Ordem de Serviço. O corpo da mensagem será copiado integralmente para o campo Descrição detalhada da OS e o anexo será adicionado conforme configurado no processo.

Novo Email

Após o envio, quando processado pela máquina de processos será associado ao devido processo e então será gerada a Ordem de Serviço:

Ordem de Serviço
