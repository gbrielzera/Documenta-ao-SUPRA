# Ativo

Caminho: Customização > Modelo de objetos > Ativos > Modelo > Ativo

Indica que o Modelo está ativo no sistema

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Modelo de identificador 1
modelo = Modelo.Carrega(1)
# modifica a propriedade Ativo
modelo.Ativo = true;
# salva modificação da propriedade Ativo
Modelo.Salva(modelo)
```
