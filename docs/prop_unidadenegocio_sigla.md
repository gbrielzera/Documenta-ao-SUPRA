# Sigla

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Sigla

Nome resumido (código) utilizado para identificar uma Unidade de Negócio

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto UnidadeNegocio de identificador 1
unidadeNegocio = UnidadeNegocio.Carrega(1)
# modifica a propriedade Sigla
unidadeNegocio.Sigla = "SP";
# salva modificação da propriedade Sigla
UnidadeNegocio.Salva(unidadeNegocio)
```
