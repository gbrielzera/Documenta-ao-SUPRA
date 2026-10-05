# HabilitaConsultaAutomaticaBaseConhecimento

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > HabilitaConsultaAutomaticaBaseConhecimento

Indica que Ordens de Serviço deste Subprocesso acionam a busca automática de artigos da Base de Conhecimento a partir dos campos Assunto, Descrição detalhada ou Sintoma analisado. Esta busca ocorre quando o usuário visualiza a tela de edição da Ordem de Serviço, quando os campos citados são utilizados como critério de recuperação por palavras-chave.

**Exemplo 1: modificação da propriedade HabilitaConsultaAutomaticaBaseConhecimento**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade HabilitaConsultaAutomaticaBaseConhecimento
classeSubProcesso.HabilitaConsultaAutomaticaBaseConhecimento = true;
# salva modificação da propriedade HabilitaConsultaAutomaticaBaseConhecimento
ClasseSubProcesso.Salva(classeSubProcesso)
```
