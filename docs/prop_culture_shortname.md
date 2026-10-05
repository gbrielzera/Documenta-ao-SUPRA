# ShortName

Caminho: Customização > Modelo de objetos > Utilitários > Culture > ShortName

Nome resumido que identifica uma Cultura na tecnologia Microsoft.NET

**Exemplo 1: modificação da propriedade ShortName**

```
# carrega objeto Culture de identificador 1
culture = Culture.Carrega(1)
# modifica a propriedade ShortName
culture.ShortName = "Short name";
# salva modificação da propriedade ShortName
Culture.Salva(culture)
```
