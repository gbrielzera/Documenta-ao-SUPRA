# Propriedade ProcedimentoInterno

Caminho: Propriedade ProcedimentoInterno

Indica que o Sub-Processo é um Procedimento interno e, desta forma, não pode ser solicitado por um Usuário.

**Exemplo 1: modificação da propriedade ProcedimentoInterno**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade ProcedimentoInterno
classeSubProcesso.ProcedimentoInterno = true;
# salva modificação da propriedade ProcedimentoInterno
ClasseSubProcesso.Salva(classeSubProcesso)
```
