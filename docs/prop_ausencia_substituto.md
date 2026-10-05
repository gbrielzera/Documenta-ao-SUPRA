# Substituto

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > Substituto

Pessoa substituto para durante período de duração da ausencia.

**Exemplo 1: modificação da propriedade Substituto**

```
# carrega objeto Ausencia de identificador 51
ausencia = Ausencia.Carrega(51)
# modifica a propriedade Substituto
ausencia.Substituto = Pessoa.Carrega(94);
# salva modificação da propriedade Substituto
Ausencia.Salva(ausencia)
```
