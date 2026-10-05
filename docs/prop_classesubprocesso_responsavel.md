# Responsavel

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > Responsavel

Pessoa responsável pelo Subprocesso

**Exemplo 1: modificação da propriedade Responsavel**

```
# carrega objeto ClasseSubProcesso de identificador 78
classeSubProcesso = ClasseSubProcesso.Carrega(78)
# modifica a propriedade Responsavel
classeSubProcesso.Responsavel = Pessoa.Carrega(23);
# salva modificação da propriedade Responsavel
ClasseSubProcesso.Salva(classeSubProcesso)
```
