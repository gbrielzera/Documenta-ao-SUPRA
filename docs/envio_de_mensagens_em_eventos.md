# Envio de Mensagens em Eventos

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 11: Envio de Comunicados > Envio de Mensagens em Eventos

## Tipos de Eventos

Uma ocorrência pode executar uma série de eventos no decorrer de sua existência. Tipos de Eventos são os eventos possíveis dentro deste ciclo de vida. Para acessar este cadastro, no menu principal selecione **Processo | Processos | Tipos de Evento**.

Os principais Tipos de Eventos são:

| **Nome** | **Descrição** |
|---|---|
| **Abertura** | Ocorre durante na Abertura. |
| **Agendamento** | Ocorre quando é a Ocorrência tem seu atendimento Agendado. |
| **Aprovação** | Ocorre quando um Aprovador de versão Versão efetua uma Aprovação. |
| **Aprovação Versão** | Ocorre quando uma Versão de um Assunto para Aprovação é Aprovada. |
| **Cancelamento** | Ocorre quando uma Ordem de Serviço é Cancelada. |
| **Cancelar Aprovação** | Ocorre ao Cancelar uma Versão submetida para Aprovação. |
| **Classificação** | Ocorre quando o atendente realiza a Classificação quanto ao Processo/Subprocesso. |
| **Comentário** | Ocorre quando um Técnico adiciona um comentário. |
| **Contato Cliente** | Ocorre quando o Técnico realiza um contatou ou tentativa de contato com Cliente. |
| **Devolução** | Ocorre quando o Analista de Implantação detecta problemas relativos a Processo. |
| **Encaminhar** | Ocorre sempre que uma Ordem de Serviço é encaminhada para um solucionador ou fila compartilhada. Neste último caso o email é redirecionado para todos os solucionadores ativos e lotados no mesmo grupo da fila. Quando o encaminhamento é realizado para **Sistema** nenhum email é enviado. |
| **Incremento Nível SLA** | Ocorre quando é excedido o tempo máximo de um nível SLA. |
| **Inicio Aprovação** | Ocorre ao Iniciar um Processo de Aprovação. |
| **Priorização** | Ocorre quando é definida a Prioridade de uma Ocorrência. |
| **Reabertura** | Ocorre quando uma Ordem de Serviço é Reaberta. |
| **Reprovação** | Ocorre quando um Aprovador de versão Versão efetua uma Reprovação. |
| **Reprovação Versão** | Ocorre quando uma Versão de um Assunto para Aprovação é Reprovada. |

Eventos disponíveis no sistema

Estes acima são cadastrados automaticamente pelo Supravizio. O evento do cadastro da figura abaixo é executado toda vez que ocorre um Inicio de Aprovação em uma Ordens de Serviço.

Cadastro de um tipo de evento

Ao ser executado o evento, é possível enviar um ou mais comunicados. Para isso, vamos criar uma nova mensagem selecionando a aba Mensagem:

Configuração de uma mensagem

### Realizando a configuração da mensagem

Existem basicamente duas formas de se cadastrar a mensagem que será enviada para os destinatários:

## Por Modelo de Comunicado

Podemos designar a mensagem que será enviada, o usuário poderá utilizar um [Modelo de Comunicado](modelos_de_comunicados). Basta selecionar o modelo adequado para isto, como na figura:

Cadastro da nova mensagem

Utilizamos para este exemplo o seguinte modelo:

Modelo utilizado na mensagem

Caso o evento seja executado, o Supravizio obtem o modelo configurado no Tipo de Evento e preenche dinamicamente os campos indicados de acordo com a Ordem de Serviço associada com a operação, como em nosso exemplo, de aprovação:

Resultado final

Após selecionar o Modelo de Comunicado, é necessário selecionar o(s) destinatário(s) do email. Isso é feito através do campo Destinatários, que é a listagem de [Papeis de Processo](papelclassenegocio_sub) cadastrados no Supravizio. Em situações onde for necessário incluir mais de um destinatário podemos fazer o uso de papéis compostos. Exemplo: para enviar email para o cliente e seu gerente poderíamos usar um papel "Cliente e Gerente do Cliente" cujo cadastro possui a aba de papéis para composição preenchida com os papéis "Cliente" e "Gerente do Cliente".

**Importante: as pessoas recuperadas por meio de papéis são incluídas na lista de destinatários se, e somente se, possuirem o campo email cadastrado.**

A lista de destinatários resultante da configuração acima pode ser modificada pelo script da mensagem.

### Por Script de mensagem

A outra forma de cadastrar um comunicado para um evento é utilizando scripts, selecionando a aba Mensagem. Neste é necessário indicar não só o corpo do email, mas também sua lista de destinatários e remetente:

Exemplo de script para configuração de mensagem

Abaixo apresentamos detalhes sobre a configuração de cada característica do comunicado:

Mensagem.Assunto

Esta mensagem configura o texto de assunto do comunicado.

Exemplo:

Mensagem.Assunto = "Apresentação de proposta comercial"

**Mensagem.Remetente**

Define o endereço utilizado como remetente. Se não for preenchido é utilizado o campo de email cadastrado no registro Sistema do cadastro de Pessoas.

Exemplo:

```
OrdemServico.Responsavel.Email
```

No exemplo acima utilizaremos o email do responsável pela Ordem de Serviço como remetente.

**Mensagem.Corpo**

Conteúdo html para o corpo do email.

**Mensagem.Destinatarios**

Lista de emails (em formato texto) dos destinatários. Para incluir itens utilize o método Mensagem.Destinatarios.Add("email@dominio.com.br").

Exemplo:

```
Mensagem.Destinatarios.Add(OrdemServico.Cliente.Email)
Mensagem.Destinatarios.Add("servicedesk@dominio.com.br")
```

No exemplo acima existirão dois destinatários: o cliente e o email de service desk. O script pode ser utilizado para modificar destinatários configurados no campo onde indicamos o papel para seleção de destinatários.

**Mensagem.Cancelar**

Campo lógico que indica ao sistema que a mensagem não deve ser enviada.

Exemplo:

```
if OrdemServico.Situacao != "Aberta":
    Mensagem.Cancelar = True
```

No exemplo acima se a Ordem de Serviço ainda não estiver aberta então a mensagem é cancelada.

**Configurações de características de comunicados**

## IMPORTANTE:

- Repare no cadastro de uma mensagem em um tipo de evento que é possível cadastrar um modelo de comunicado e seus destinatários e na aba Mensagem cadastrarmos um script para geração da mensagem, porém, nesta mensagem, o cadastro que prevalece para a geração de mensagem é o do script configurado, ou seja, o script pode ser utilizado para adicionar configurações previamente realizadas nos campos cadastrados na mensagem.
- O campo Processo alvo de uma mensagem de tipo de evento é válido tanto para geração da mensagem por modelo de comunicado, quanto para script.

### Temporalidade

A temporalidade é um prazo em dias de permanência da mensagem no banco de dados. Ao terminar o prazo da temporalidade a mensagem será removida automaticamente.

O seu uso é indicado para redução de uso de espaço em disco após um período no qual a sua manutenção já não é mais necessária. Exemplo: após 6 meses de envio já não seria mais necessário manter no banco uma mensagem solicitando aprovação de uma Ordem de Serviço ou avisando algum solucionador sobre a chegada de uma Ordem de Serviço em sua fila.
