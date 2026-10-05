# Id

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Report

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade Id
userReport.Id = 1;
# salva modificação da propriedade Id
UserReport.Salva(userReport)
```
