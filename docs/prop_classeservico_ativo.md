# Ativo

Caminho: Customização > Modelo de objetos > Processo > ClasseServico > Ativo

Indica que o Tipo de Serviço está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto ClasseServico de identificador 1
classeServico = ClasseServico.Carrega(1)
# modifica a propriedade Ativo
classeServico.Ativo = true;
# salva modificação da propriedade Ativo
ClasseServico.Salva(classeServico)
```
