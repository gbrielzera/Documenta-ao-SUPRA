# ComentarioObrigatorio

Caminho: Customização > Modelo de objetos > Recurso > MotivoInterrupcaoSLA > ComentarioObrigatorio

Quando ativado obriga o usuário que estiver registrando a interrupção (somente inclusão manual) a informar um motivo. Este motivo é replicado no campo de comentários e publicado no Autoatendimento.

**Exemplo 1: modificação da propriedade ComentarioObrigatorio**

```
# carrega objeto MotivoInterrupcaoSLA de identificador 1
motivoInterrupcaoSLA = MotivoInterrupcaoSLA.Carrega(1)
# modifica a propriedade ComentarioObrigatorio
motivoInterrupcaoSLA.ComentarioObrigatorio = true;
# salva modificação da propriedade ComentarioObrigatorio
MotivoInterrupcaoSLA.Salva(motivoInterrupcaoSLA)
```
