# Id

Caminho: Customização > Modelo de objetos > Recurso > Orgao > Id

Identificador do Órgão

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Orgao de identificador 1
orgao = Orgao.Carrega(1)
# modifica a propriedade Id
orgao.Id = 1;
# salva modificação da propriedade Id
Orgao.Salva(orgao)
```
