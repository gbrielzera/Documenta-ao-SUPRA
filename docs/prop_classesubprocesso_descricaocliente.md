# DescricaoCliente

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > DescricaoCliente

Descritivo apresentado para o Cliente. Se não for preenchido é apresentado o Descritivo padrão do Tipo de Subprocesso.

**Exemplo 1: modificação da propriedade DescricaoCliente**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade DescricaoCliente
classeSubProcesso.DescricaoCliente = "Descritivo cliente";
# salva modificação da propriedade DescricaoCliente
ClasseSubProcesso.Salva(classeSubProcesso)
```
