# Descricao

Caminho: Customização > Modelo de objetos > Ativos > Fabricante > Descricao

Descrição detalhada do Fabricante

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Fabricante de identificador 1
fabricante = Fabricante.Carrega(1)
# modifica a propriedade Descricao
fabricante.Descricao = "HP";
# salva modificação da propriedade Descricao
Fabricante.Salva(fabricante)
```
