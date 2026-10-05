# AcessoTotalAdmin

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > AcessoTotalAdmin

Indica que usuários com o perfil Administrador possuem acesso total em ocorrências do Subprocesso.

**Exemplo 1: modificação da propriedade AcessoTotalAdmin**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade AcessoTotalAdmin
classeSubProcesso.AcessoTotalAdmin = true;
# salva modificação da propriedade AcessoTotalAdmin
ClasseSubProcesso.Salva(classeSubProcesso)
```
