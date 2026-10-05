# Descricao

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > Descricao

Texto que descreve claramente o objetivo do Grupo de Trabalho. Este texto é utilizado em diversas telas e relatórios da aplicação Supravizio.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade Descricao
grupoTrabalho.Descricao = "Coordenação de Suporte";
# salva modificação da propriedade Descricao
GrupoTrabalho.Salva(grupoTrabalho)
```
