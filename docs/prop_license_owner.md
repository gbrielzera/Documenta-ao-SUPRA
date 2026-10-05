# Owner

Caminho: Customização > Modelo de objetos > Utilitários > License > Owner

Proprietário da licença de uso.

**Exemplo 1: modificação da propriedade Owner**

```
# carrega objeto License de identificador 1
license = License.Carrega(1)
# modifica a propriedade Owner
license.Owner = "Venki Tecnologia";
# salva modificação da propriedade Owner
License.Salva(license)
```
