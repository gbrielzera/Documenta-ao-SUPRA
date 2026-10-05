# Cliente

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Cliente

Cliente que solicitou o Serviço

**Exemplo 1: modificação da propriedade Cliente**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade Cliente
ocorrencia.Cliente = Pessoa.Carrega(23);
# salva modificação da propriedade Cliente
Ocorrencia.Salva(ocorrencia)
```
