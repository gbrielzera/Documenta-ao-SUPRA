# Patrimonio

Caminho: Customização > Modelo de objetos > Ativos > Hardware > Patrimonio

Identificação de Patrimonio

**Exemplo 1: modificação da propriedade Patrimonio**

```
# carrega objeto Hardware de identificador 1
hardware = Hardware.Carrega(1)
# modifica a propriedade Patrimonio
hardware.Patrimonio = "Patrimonio";
# salva modificação da propriedade Patrimonio
Hardware.Salva(hardware)
```
