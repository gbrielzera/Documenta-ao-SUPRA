# Motivo

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > Motivo

Motivo para a ausência

**Exemplo 1: modificação da propriedade Motivo**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade Motivo
ausencia.Motivo = "Motivo";
# salva modificação da propriedade Motivo
Ausencia.Salva(ausencia)
```
