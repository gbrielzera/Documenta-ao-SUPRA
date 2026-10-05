# DescricaoCampoDataHora1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoDataHora1

Descrição para entrada de dados no Campo Data/hora 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoDataHora1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoDataHora1
classeApontamento.DescricaoCampoDataHora1 = "Descrição Data/hora 1";
# salva modificação da propriedade DescricaoCampoDataHora1
ClasseApontamento.Salva(classeApontamento)
```
