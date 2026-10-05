# CopiasLicenciadas

Caminho: Customização > Modelo de objetos > Ativos > Software > CopiasLicenciadas

Número de cópias licenciadas

**Exemplo 1: modificação da propriedade CopiasLicenciadas**

```
# carrega objeto Software de identificador 1
software = Software.Carrega(1)
# modifica a propriedade CopiasLicenciadas
software.CopiasLicenciadas = 1;
# salva modificação da propriedade CopiasLicenciadas
Software.Salva(software)
```
