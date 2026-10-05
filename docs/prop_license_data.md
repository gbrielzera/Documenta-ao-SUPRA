# Data

Caminho: Customização > Modelo de objetos > Utilitários > License > Data

Informações criptografadas sobre o licenciamento

**Exemplo 1: modificação da propriedade Data**

```
# carrega objeto License de identificador 1
license = License.Carrega(1)
# modifica a propriedade Data
license.Data = "Dados";
# salva modificação da propriedade Data
License.Salva(license)
```
