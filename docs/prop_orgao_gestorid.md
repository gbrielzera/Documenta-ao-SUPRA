# GestorId

Caminho: Customização > Modelo de objetos > Recurso > Orgao > GestorId

Identificador do Gestor do Órgão. Esta associação é utilizada constantemente na implementação de Processos.

**Exemplo 1: modificação da propriedade GestorId**

```
# carrega objeto Orgao de identificador 1
orgao = Orgao.Carrega(1)
# modifica a propriedade GestorId
orgao.GestorId = 1;
# salva modificação da propriedade GestorId
Orgao.Salva(orgao)
```
