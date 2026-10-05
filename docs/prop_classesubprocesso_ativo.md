# Ativo

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > Ativo

Indica que o Tipo de Subprocesso está Ativo. Quando ativo o tipo é visível em formulários de entrada de dados para Ordens de Serviço ou Consultas diversas.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade Ativo
classeSubProcesso.Ativo = true;
# salva modificação da propriedade Ativo
ClasseSubProcesso.Salva(classeSubProcesso)
```
