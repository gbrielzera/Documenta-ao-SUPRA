# GrupoTrabalho

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > GrupoTrabalho

Grupo de Trabalho responsável

**Exemplo 1: modificação da propriedade GrupoTrabalho**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade GrupoTrabalho
ocorrencia.GrupoTrabalho = GrupoTrabalho.Carrega(23);
# salva modificação da propriedade GrupoTrabalho
Ocorrencia.Salva(ocorrencia)
```
