# GruposTrabalhoAutorizados

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao > GruposTrabalhoAutorizados

Grupos de Trabalho que estão autorizados a visualizar o resultado da apuração de indicadores.

**Exemplo 1: percorrer objetos da propriedade GruposTrabalhoAutorizados**

```
# carrega objeto PlanoGestao de identificador 78
planoGestao = PlanoGestao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if planoGestao != None:
    # percorre objetos da propriedade GruposTrabalhoAutorizados e para cada uma escreve conteúdo no log de mensagens
    for grupoTrabalhoAutorizado in planoGestao.GruposTrabalhoAutorizados:
        Utils.LogInformation(grupoTrabalhoAutorizado.ToString())
```
