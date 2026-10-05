# Id

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseApontamento

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade Id
classeApontamento.Id = 1;
# salva modificação da propriedade Id
ClasseApontamento.Salva(classeApontamento)
```
