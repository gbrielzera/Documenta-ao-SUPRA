# ClasseNegocio

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > ClasseNegocio

Classe de negócio da Ocorrência onde será aplicado o Método de Priorização.

**Exemplo 1: modificação da propriedade ClasseNegocio**

```
# carrega objeto MetodoPriorizacao de identificador 1
metodoPriorizacao = MetodoPriorizacao.Carrega(1)
# modifica a propriedade ClasseNegocio
metodoPriorizacao.ClasseNegocio = "OrdemServico";
# salva modificação da propriedade ClasseNegocio
MetodoPriorizacao.Salva(metodoPriorizacao)
```
