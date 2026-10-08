# Propriedade CodigoRecuperacao

Caminho: Propriedade CodigoRecuperacao

Código de Recuperação

**Exemplo 1: modificação da propriedade CodigoRecuperacao**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade CodigoRecuperacao
ocorrencia.CodigoRecuperacao = "Código recuperação";
# salva modificação da propriedade CodigoRecuperacao
Ocorrencia.Salva(ocorrencia)
```
