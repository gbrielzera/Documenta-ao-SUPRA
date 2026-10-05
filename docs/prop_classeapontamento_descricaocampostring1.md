# DescricaoCampoString1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoString1

Descrição para entrada de dados no Campo String 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoString1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoString1
classeApontamento.DescricaoCampoString1 = "Descrição String 1";
# salva modificação da propriedade DescricaoCampoString1
ClasseApontamento.Salva(classeApontamento)
```
