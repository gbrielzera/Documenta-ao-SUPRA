# Id

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um GrupoTrabalho

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade Id
grupoTrabalho.Id = 1;
# salva modificação da propriedade Id
GrupoTrabalho.Salva(grupoTrabalho)
```
