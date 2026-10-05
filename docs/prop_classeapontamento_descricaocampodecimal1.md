# DescricaoCampoDecimal1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoDecimal1

Descrição para entrada de dados no Campo Decimal 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoDecimal1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoDecimal1
classeApontamento.DescricaoCampoDecimal1 = "Descrição Decimal 1";
# salva modificação da propriedade DescricaoCampoDecimal1
ClasseApontamento.Salva(classeApontamento)
```
