# ReferenciaCircular

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ReferenciaCircular

Indica que em algum momento da execução do processo ocorrêu um Loop infinito caracterizando referência circular entre as atividades de processos.

**Exemplo 1: modificação da propriedade ReferenciaCircular**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade ReferenciaCircular
ocorrencia.ReferenciaCircular = true;
# salva modificação da propriedade ReferenciaCircular
Ocorrencia.Salva(ocorrencia)
```
