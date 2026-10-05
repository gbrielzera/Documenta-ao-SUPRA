# SuperClasseServico

Caminho: Customização > Modelo de objetos > Processo > GrupoServico > SuperClasseServico

Nível mais elevado na hierarquia de classificações de Serviços.

**Exemplo 1: modificação da propriedade SuperClasseServico**

```
# carrega objeto GrupoServico de identificador 78
grupoServico = GrupoServico.Carrega(78)
# modifica a propriedade SuperClasseServico
grupoServico.SuperClasseServico = SuperClasseServico.Carrega(23);
# salva modificação da propriedade SuperClasseServico
GrupoServico.Salva(grupoServico)
```
