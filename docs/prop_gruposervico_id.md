# Id

Caminho: Customização > Modelo de objetos > Processo > GrupoServico > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um GrupoServico

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto GrupoServico de identificador 1
grupoServico = GrupoServico.Carrega(1)
# modifica a propriedade Id
grupoServico.Id = 1;
# salva modificação da propriedade Id
GrupoServico.Salva(grupoServico)
```
