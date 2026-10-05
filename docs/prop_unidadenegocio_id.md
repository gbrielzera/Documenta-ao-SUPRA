# Id

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Id

Número sequencial gerado por sistema para identificar uma Unidade de Negócio. Este número não pode ser modificado pelo usuário do sistema.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto UnidadeNegocio de identificador 1
unidadeNegocio = UnidadeNegocio.Carrega(1)
# modifica a propriedade Id
unidadeNegocio.Id = 1;
# salva modificação da propriedade Id
UnidadeNegocio.Salva(unidadeNegocio)
```
