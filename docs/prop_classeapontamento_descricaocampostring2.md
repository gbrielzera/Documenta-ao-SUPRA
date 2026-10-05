# DescricaoCampoString2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoString2

Descrição para entrada de dados no Campo String 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoString2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoString2
classeApontamento.DescricaoCampoString2 = "Descrição String 2";
# salva modificação da propriedade DescricaoCampoString2
ClasseApontamento.Salva(classeApontamento)
```
