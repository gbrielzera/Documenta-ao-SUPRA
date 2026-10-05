# Id

Caminho: Customização > Modelo de objetos > Utilitários > License > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um License

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto License de identificador 1
license = License.Carrega(1)
# modifica a propriedade Id
license.Id = 1;
# salva modificação da propriedade Id
License.Salva(license)
```
