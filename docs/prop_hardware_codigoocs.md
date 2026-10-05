# CodigoOCS

Caminho: Customização > Modelo de objetos > Ativos > Hardware > CodigoOCS

Código do hardware original do banco de dados OCS

**Exemplo 1: modificação da propriedade CodigoOCS**

```
# carrega objeto Hardware de identificador 1
hardware = Hardware.Carrega(1)
# modifica a propriedade CodigoOCS
hardware.CodigoOCS = "Código OCS";
# salva modificação da propriedade CodigoOCS
Hardware.Salva(hardware)
```
