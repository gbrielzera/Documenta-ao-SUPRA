# Local

Caminho: Customização > Modelo de objetos > Ativos > Hardware > Local

Localização do Equipamento

**Exemplo 1: modificação da propriedade Local**

```
# carrega objeto Hardware de identificador 73
hardware = Hardware.Carrega(73)
# modifica a propriedade Local
hardware.Local = Local.Carrega(91);
# salva modificação da propriedade Local
Hardware.Salva(hardware)
```
