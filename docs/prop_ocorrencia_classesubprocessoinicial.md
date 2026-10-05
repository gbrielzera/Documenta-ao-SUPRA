# ClasseSubProcessoInicial

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ClasseSubProcessoInicial

Tipo de de Subprocesso inicialmente atribuído para a Ocorrência.

**Exemplo 1: modificação da propriedade ClasseSubProcessoInicial**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade ClasseSubProcessoInicial
ocorrencia.ClasseSubProcessoInicial = ClasseSubProcesso.Carrega(23);
# salva modificação da propriedade ClasseSubProcessoInicial
Ocorrencia.Salva(ocorrencia)
```
