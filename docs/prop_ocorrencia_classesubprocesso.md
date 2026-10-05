# ClasseSubProcesso

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ClasseSubProcesso

Um Tipo de Subprocesso mantém características de um fluxo que são invariáveis entre suas diversas versões.

**Exemplo 1: modificação da propriedade ClasseSubProcesso**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade ClasseSubProcesso
ocorrencia.ClasseSubProcesso = ClasseSubProcesso.Carrega(23);
# salva modificação da propriedade ClasseSubProcesso
Ocorrencia.Salva(ocorrencia)
```
