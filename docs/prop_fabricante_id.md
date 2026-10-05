# Id

Caminho: Customização > Modelo de objetos > Ativos > Fabricante > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Fabricante

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Fabricante de identificador 1
fabricante = Fabricante.Carrega(1)
# modifica a propriedade Id
fabricante.Id = 1;
# salva modificação da propriedade Id
Fabricante.Salva(fabricante)
```
