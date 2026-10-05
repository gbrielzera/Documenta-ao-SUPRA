# FabricanteId

Caminho: Customização > Modelo de objetos > Ativos > Modelo > FabricanteId

Identificador do Fabricante associado ao Modelo

**Exemplo 1: modificação da propriedade FabricanteId**

```
# carrega objeto Modelo de identificador 1
modelo = Modelo.Carrega(1)
# modifica a propriedade FabricanteId
modelo.FabricanteId = 1;
# salva modificação da propriedade FabricanteId
Modelo.Salva(modelo)
```
