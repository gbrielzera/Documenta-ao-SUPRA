# Empresa

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Empresa

Empresa para a qual a Unidade pertence. Este campo é utilizado como critério de filtro para os locais exibidos na abertura de Ordens de Serviço do Autoatendimento. Se o usuário conectado estiver associado a uma empresa pertencente a um grupo de empresas, então são exibidas todas as unidades do grupo. Se sua empresa não estiver associada a um grupo então são exibidas as unidades da empresa.

**Exemplo 1: modificação da propriedade Empresa**

```
# carrega objeto UnidadeNegocio de identificador 51
unidadeNegocio = UnidadeNegocio.Carrega(51)
# modifica a propriedade Empresa
unidadeNegocio.Empresa = Empresa.Carrega(94);
# salva modificação da propriedade Empresa
UnidadeNegocio.Salva(unidadeNegocio)
```
