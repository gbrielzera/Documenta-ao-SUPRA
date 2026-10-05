# DescricaoCampoInteiro1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoInteiro1

Descrição para entrada de dados no Campo Inteiro 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoInteiro1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoInteiro1
classeApontamento.DescricaoCampoInteiro1 = "Descrição Inteiro 1";
# salva modificação da propriedade DescricaoCampoInteiro1
ClasseApontamento.Salva(classeApontamento)
```
