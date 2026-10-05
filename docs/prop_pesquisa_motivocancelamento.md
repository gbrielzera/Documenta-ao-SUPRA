# MotivoCancelamento

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > MotivoCancelamento

Motivo de Cancelamento da Pesquisa

**Exemplo 1: modificação da propriedade MotivoCancelamento**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade MotivoCancelamento
pesquisa.MotivoCancelamento = "Motivo cancelamento";
# salva modificação da propriedade MotivoCancelamento
Pesquisa.Salva(pesquisa)
```
