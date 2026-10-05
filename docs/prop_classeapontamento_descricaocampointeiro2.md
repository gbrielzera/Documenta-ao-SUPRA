# DescricaoCampoInteiro2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoInteiro2

Descrição para entrada de dados no Campo Inteiro 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoInteiro2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoInteiro2
classeApontamento.DescricaoCampoInteiro2 = "Descrição Inteiro 2";
# salva modificação da propriedade DescricaoCampoInteiro2
ClasseApontamento.Salva(classeApontamento)
```
