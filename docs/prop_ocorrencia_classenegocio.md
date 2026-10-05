# ClasseNegocio

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ClasseNegocio

Classe de Negócio que implementa a Token. Este valor é alimentado automaticamente pelo sistema assim que o item é Classficado.

**Exemplo 1: modificação da propriedade ClasseNegocio**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade ClasseNegocio
ocorrencia.ClasseNegocio = "OrdemServico";
# salva modificação da propriedade ClasseNegocio
Ocorrencia.Salva(ocorrencia)
```
