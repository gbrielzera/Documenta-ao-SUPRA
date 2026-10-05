# Sigla

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > Sigla

Nome resumido (código) utilizado para identificar um Grupo de Trabalho.

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade Sigla
grupoTrabalho.Sigla = "SUPORTE";
# salva modificação da propriedade Sigla
GrupoTrabalho.Salva(grupoTrabalho)
```
