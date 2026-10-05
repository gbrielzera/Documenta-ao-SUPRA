# Descricao

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Descricao

Texto que descreve claramente a localização ou finalidade da Unidade de Negócio

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto UnidadeNegocio de identificador 1
unidadeNegocio = UnidadeNegocio.Carrega(1)
# modifica a propriedade Descricao
unidadeNegocio.Descricao = "São Paulo";
# salva modificação da propriedade Descricao
UnidadeNegocio.Salva(unidadeNegocio)
```
