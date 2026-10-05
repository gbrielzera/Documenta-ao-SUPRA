# SolicitacaoServicos

Caminho: Customização > Modelo de objetos > Processo > Servico > SolicitacaoServicos

Detalhes sobre procedimento de abertura de Chamados. Se não for preenchido é estabelecido o procedimento padrão por meio do Catálogo de Serviços.

**Exemplo 1: modificação da propriedade SolicitacaoServicos**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade SolicitacaoServicos
servico.SolicitacaoServicos = "Solicitação Serviços";
# salva modificação da propriedade SolicitacaoServicos
Servico.Salva(servico)
```
