# ReferenciaLicenca

Caminho: Customização > Modelo de objetos > Ativos > Software > ReferenciaLicenca

Dados de referência para o Licenciamento do Software

**Exemplo 1: modificação da propriedade ReferenciaLicenca**

```
# carrega objeto Software de identificador 1
software = Software.Carrega(1)
# modifica a propriedade ReferenciaLicenca
software.ReferenciaLicenca = "Referência licenciamento";
# salva modificação da propriedade ReferenciaLicenca
Software.Salva(software)
```
