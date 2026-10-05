# Id

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > Id

Número sequencial gerado automaticamente pelo sistema para identificar um Tipo de Subprocesso. Um Identificador não pode ser modificado pelo usuário.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade Id
classeSubProcesso.Id = 1;
# salva modificação da propriedade Id
ClasseSubProcesso.Salva(classeSubProcesso)
```
