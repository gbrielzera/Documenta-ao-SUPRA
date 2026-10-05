# FraseInversaAssociacao

Caminho: Customização > Modelo de objetos > Processo > Associacao > FraseInversaAssociacao

Frase utilizada para representar o sentido inverso da Associação.

**Exemplo 1: modificação da propriedade FraseInversaAssociacao**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade FraseInversaAssociacao
associacao.FraseInversaAssociacao = "Incidente que gerou o Problema";
# salva modificação da propriedade FraseInversaAssociacao
Associacao.Salva(associacao)
```
