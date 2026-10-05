# ClasseNegocio

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > ClasseNegocio

Classe de Negócio dos Processos onde será publicado o Papel.

**Exemplo 1: modificação da propriedade ClasseNegocio**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade ClasseNegocio
papelClasseNegocio.ClasseNegocio = "OrdemServico";
# salva modificação da propriedade ClasseNegocio
PapelClasseNegocio.Salva(papelClasseNegocio)
```
