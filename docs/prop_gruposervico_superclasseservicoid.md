# SuperClasseServicoId

Caminho: Customização > Modelo de objetos > Processo > GrupoServico > SuperClasseServicoId

Identificador da Classe de Serviço associada

**Exemplo 1: modificação da propriedade SuperClasseServicoId**

```
# carrega objeto GrupoServico de identificador 1
grupoServico = GrupoServico.Carrega(1)
# modifica a propriedade SuperClasseServicoId
grupoServico.SuperClasseServicoId = 1;
# salva modificação da propriedade SuperClasseServicoId
GrupoServico.Salva(grupoServico)
```
