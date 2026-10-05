# Fabricante

Caminho: Customização > Modelo de objetos > Ativos > Modelo > Fabricante

Fabricante do Modelo

**Exemplo 1: modificação da propriedade Fabricante**

```
# carrega objeto Modelo de identificador 73
modelo = Modelo.Carrega(73)
# modifica a propriedade Fabricante
modelo.Fabricante = Fabricante.Carrega(91);
# salva modificação da propriedade Fabricante
Modelo.Salva(modelo)
```
