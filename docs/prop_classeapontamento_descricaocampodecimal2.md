# DescricaoCampoDecimal2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoDecimal2

Descrição para entrada de dados no Campo Decimal 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoDecimal2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoDecimal2
classeApontamento.DescricaoCampoDecimal2 = "Descrição Decimal 2";
# salva modificação da propriedade DescricaoCampoDecimal2
ClasseApontamento.Salva(classeApontamento)
```
