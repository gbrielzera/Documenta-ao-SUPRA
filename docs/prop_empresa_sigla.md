# Sigla

Caminho: Customização > Modelo de objetos > Recurso > Empresa > Sigla

Nome resumido utilizado para identificar uma Empresa

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto Empresa de identificador 1
empresa = Empresa.Carrega(1)
# modifica a propriedade Sigla
empresa.Sigla = "VENKI";
# salva modificação da propriedade Sigla
Empresa.Salva(empresa)
```
