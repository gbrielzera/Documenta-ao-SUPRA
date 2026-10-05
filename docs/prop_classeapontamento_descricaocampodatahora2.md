# DescricaoCampoDataHora2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > DescricaoCampoDataHora2

Descrição para entrada de dados no Campo Data/hora 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados.

**Exemplo 1: modificação da propriedade DescricaoCampoDataHora2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade DescricaoCampoDataHora2
classeApontamento.DescricaoCampoDataHora2 = "Decrição Data/hora 2";
# salva modificação da propriedade DescricaoCampoDataHora2
ClasseApontamento.Salva(classeApontamento)
```
