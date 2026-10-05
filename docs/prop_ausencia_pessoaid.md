# PessoaId

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > PessoaId

Identificador da Pessoa para qual foi registrado o período de Ausencia

**Exemplo 1: modificação da propriedade PessoaId**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade PessoaId
ausencia.PessoaId = 1;
# salva modificação da propriedade PessoaId
Ausencia.Salva(ausencia)
```
