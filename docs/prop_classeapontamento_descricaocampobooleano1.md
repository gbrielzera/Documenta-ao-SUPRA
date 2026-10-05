# DescricaoCampoBooleano1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoBooleano1

Descrição para entrada de dados no Campo Booleano 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoBooleano1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoBooleano1
classeApontamento.DescricaoCampoBooleano1 = "Descrição Booleano 1";
# salva modificação da propriedade DescricaoCampoBooleano1
ClasseApontamento.Salva(classeApontamento)
```
