# Localizacao

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Localizacao

Endereço, Cidade, Estado ou qualquer outra referência de Localização da Unidade de Negócio.

**Exemplo 1: modificação da propriedade Localizacao**

```
# carrega objeto UnidadeNegocio de identificador 1
unidadeNegocio = UnidadeNegocio.Carrega(1)
# modifica a propriedade Localizacao
unidadeNegocio.Localizacao = "Localização";
# salva modificação da propriedade Localizacao
UnidadeNegocio.Salva(unidadeNegocio)
```
