# EncaminharSubstituto

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > EncaminharSubstituto

Redirecionar encaminhamentos para o Substituto

**Exemplo 1: modificação da propriedade EncaminharSubstituto**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade EncaminharSubstituto
ausencia.EncaminharSubstituto = true;
# salva modificação da propriedade EncaminharSubstituto
Ausencia.Salva(ausencia)
```
