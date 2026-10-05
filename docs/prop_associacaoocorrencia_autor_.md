# Autor

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > Autor

Pessoa que estabeleceu a Associação.

**Exemplo 1: modificação da propriedade Autor**

```
# carrega objeto AssociacaoOcorrencia de identificador 78
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(78)
# modifica a propriedade Autor
associacaoOcorrencia.Autor = Pessoa.Carrega(23);
# salva modificação da propriedade Autor
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
