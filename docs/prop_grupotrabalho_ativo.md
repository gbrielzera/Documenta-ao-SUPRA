# Ativo

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > Ativo

Indica que o Grupo de Trabalho está ativo. Quando ativo o Grupo de Trabalho pode ser utilizado na implementação de Papéis de Processo ou para lotação de profissionais. Quando um Grupo de Trabalho se torna Inativo automaticamente todos os profissionais associados também são desativados.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade Ativo
grupoTrabalho.Ativo = true;
# salva modificação da propriedade Ativo
GrupoTrabalho.Salva(grupoTrabalho)
```
