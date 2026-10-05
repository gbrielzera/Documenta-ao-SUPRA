# PermiteSubstitutoModificar

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > PermiteSubstitutoModificar

Permitir que o Substituto modifique todas as Ordens de Serviço no período de ausência

**Exemplo 1: modificação da propriedade PermiteSubstitutoModificar**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade PermiteSubstitutoModificar
ausencia.PermiteSubstitutoModificar = true;
# salva modificação da propriedade PermiteSubstitutoModificar
Ausencia.Salva(ausencia)
```
