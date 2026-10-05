# LocalId

Caminho: Customização > Modelo de objetos > Ativos > Hardware > LocalId

Identificador da localização do Equipamento

**Exemplo 1: modificação da propriedade LocalId**

```
# carrega objeto Hardware de identificador 1
hardware = Hardware.Carrega(1)
# modifica a propriedade LocalId
hardware.LocalId = 1;
# salva modificação da propriedade LocalId
Hardware.Salva(hardware)
```
