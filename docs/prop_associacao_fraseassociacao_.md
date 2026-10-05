# FraseAssociacao

Caminho: Customização > Modelo de objetos > Processo > Associacao > FraseAssociacao

Frase utilizada para estabelecer a Associação.

**Exemplo 1: modificação da propriedade FraseAssociacao**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade FraseAssociacao
associacao.FraseAssociacao = "Problema gerado pelo Incidente";
# salva modificação da propriedade FraseAssociacao
Associacao.Salva(associacao)
```
