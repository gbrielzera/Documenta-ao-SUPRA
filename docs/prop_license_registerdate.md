# RegisterDate

Caminho: Customização > Modelo de objetos > Utilitários > License > RegisterDate

Data em que foi realizada a importação do arquivo de licenciamento do produto.

**Exemplo 1: modificação da propriedade RegisterDate**

```
# carrega objeto License de identificador 1
license = License.Carrega(1)
# modifica a propriedade RegisterDate
license.RegisterDate = DateTime;
# salva modificação da propriedade RegisterDate
License.Salva(license)
```
