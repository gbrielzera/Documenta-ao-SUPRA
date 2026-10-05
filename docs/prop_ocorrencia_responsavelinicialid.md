# ResponsavelInicialId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ResponsavelInicialId

Identificador do Solucionador que foi o primeiro responsável pela Ocorrência.

**Exemplo 1: modificação da propriedade ResponsavelInicialId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade ResponsavelInicialId
ocorrencia.ResponsavelInicialId = 1;
# salva modificação da propriedade ResponsavelInicialId
Ocorrencia.Salva(ocorrencia)
```
