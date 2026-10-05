# Ocorrencia

Caminho: Customização > Modelo de objetos > Processo > TesteControle > Ocorrencia

Ocorrência gerada para teste do Controle

**Exemplo 1: modificação da propriedade Ocorrencia**

```
# carrega objeto TesteControle de identificador 78
testeControle = TesteControle.Carrega(78)
# modifica a propriedade Ocorrencia
testeControle.Ocorrencia = Ocorrencia.Carrega(23);
# salva modificação da propriedade Ocorrencia
TesteControle.Salva(testeControle)
```
