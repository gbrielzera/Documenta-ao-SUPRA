# Id

Caminho: Customização > Modelo de objetos > Utilitários > Culture > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma Cultura

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Culture de identificador 1
culture = Culture.Carrega(1)
# modifica a propriedade Id
culture.Id = 1;
# salva modificação da propriedade Id
Culture.Salva(culture)
```
