# Ativo

Caminho: Customização > Modelo de objetos > Ativos > Fabricante > Ativo

Indica que o Fabricante está ativo no sistema

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Fabricante de identificador 1
fabricante = Fabricante.Carrega(1)
# modifica a propriedade Ativo
fabricante.Ativo = true;
# salva modificação da propriedade Ativo
Fabricante.Salva(fabricante)
```
