# GrupoServico

Caminho: Customização > Modelo de objetos > Processo > ClasseServico > GrupoServico

Segundo nível hierárquico de classificação no qual o tipo de Serviço está inserido.

**Exemplo 1: modificação da propriedade GrupoServico**

```
# carrega objeto ClasseServico de identificador 78
classeServico = ClasseServico.Carrega(78)
# modifica a propriedade GrupoServico
classeServico.GrupoServico = GrupoServico.Carrega(23);
# salva modificação da propriedade GrupoServico
ClasseServico.Salva(classeServico)
```
