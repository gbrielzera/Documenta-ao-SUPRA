# Description

Caminho: Customização > Modelo de objetos > Utilitários > Culture > Description

Descrição detalhada do Culture

**Exemplo 1: modificação da propriedade Description**

```
# carrega objeto Culture de identificador 1
culture = Culture.Carrega(1)
# modifica a propriedade Description
culture.Description = "Descrição";
# salva modificação da propriedade Description
Culture.Salva(culture)
```
