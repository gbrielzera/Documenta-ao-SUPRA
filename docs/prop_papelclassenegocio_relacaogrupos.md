# RelacaoGrupos

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > RelacaoGrupos

Relação de grupos que define a regra de recuperação de solucionadores.

**Exemplo 1: percorrer objetos da propriedade RelacaoGrupos**

```
# carrega objeto PapelClasseNegocio de identificador 78
papelClasseNegocio = PapelClasseNegocio.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if papelClasseNegocio != None:
    # percorre objetos da propriedade RelacaoGrupos e para cada uma escreve conteúdo no log de mensagens
    for grupoPapel in papelClasseNegocio.RelacaoGrupos:
        Utils.LogInformation(grupoPapel.ToString())
```
