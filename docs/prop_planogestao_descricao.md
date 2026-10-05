# Descricao

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao > Descricao

Descrição detalhada do Plano de Gestão. Esta descrição é utilizada para seleção do Plao de Gestão na aplicação Executive Dashboard.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto PlanoGestao de identificador 1
planoGestao = PlanoGestao.Carrega(1)
# modifica a propriedade Descricao
planoGestao.Descricao = "Plano de Gestão";
# salva modificação da propriedade Descricao
PlanoGestao.Salva(planoGestao)
```
