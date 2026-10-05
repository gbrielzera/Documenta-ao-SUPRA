# Numero

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Numero

Número formatado da Ocorrência

**Exemplo 1: modificação da propriedade Numero**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade Numero
ocorrencia.Numero = "Número";
# salva modificação da propriedade Numero
Ocorrencia.Salva(ocorrencia)
```
