# AtorGrupoTrabalho

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > AtorGrupoTrabalho

Critério final de seleção de uma ou mais pessoas aplicado após regras de recuperação.

**Exemplo 1: modificação da propriedade AtorGrupoTrabalho**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade AtorGrupoTrabalho
papelClasseNegocio.AtorGrupoTrabalho = "MembroMenorCarga";
# salva modificação da propriedade AtorGrupoTrabalho
PapelClasseNegocio.Salva(papelClasseNegocio)
```
