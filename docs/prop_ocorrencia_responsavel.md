# Responsavel

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Responsavel

Pessoa

**Exemplo 1: modificação da propriedade Responsavel**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade Responsavel
ocorrencia.Responsavel = Pessoa.Carrega(23);
# salva modificação da propriedade Responsavel
Ocorrencia.Salva(ocorrencia)
```
