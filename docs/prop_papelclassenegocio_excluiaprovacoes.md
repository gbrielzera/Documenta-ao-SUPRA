# ExcluiAprovacoes

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > ExcluiAprovacoes

Exclui da contagem de Ocorrências aquelas que estiveram Pendentes de Aprovação.

**Exemplo 1: modificação da propriedade ExcluiAprovacoes**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade ExcluiAprovacoes
papelClasseNegocio.ExcluiAprovacoes = true;
# salva modificação da propriedade ExcluiAprovacoes
PapelClasseNegocio.Salva(papelClasseNegocio)
```
