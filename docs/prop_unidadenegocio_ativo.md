# Ativo

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Ativo

Indica que a Unidade de Negócio está ativa

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto UnidadeNegocio de identificador 1
unidadeNegocio = UnidadeNegocio.Carrega(1)
# modifica a propriedade Ativo
unidadeNegocio.Ativo = true;
# salva modificação da propriedade Ativo
UnidadeNegocio.Salva(unidadeNegocio)
```
