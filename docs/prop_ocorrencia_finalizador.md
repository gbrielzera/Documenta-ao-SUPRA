# Finalizador

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Finalizador

Pessoa que finalizou o registro

**Exemplo 1: modificação da propriedade Finalizador**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade Finalizador
ocorrencia.Finalizador = Pessoa.Carrega(23);
# salva modificação da propriedade Finalizador
Ocorrencia.Salva(ocorrencia)
```
