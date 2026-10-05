# Predios

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Predios

Prédios contidos na Unidade de Negócio

**Exemplo 1: percorrer objetos da propriedade Predios**

```
# carrega objeto UnidadeNegocio de identificador 51
unidadeNegocio = UnidadeNegocio.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if unidadeNegocio != None:
    # percorre objetos da propriedade Predios e para cada uma escreve conteúdo no log de mensagens
    for predio in unidadeNegocio.Predios:
        Utils.LogInformation(predio.ToString())
```
