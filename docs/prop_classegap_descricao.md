# Descricao

Caminho: Customização > Modelo de objetos > Processo > ClasseGap > Descricao

Descrição detalhada do ClasseGAP

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ClasseGap de identificador 1
classeGap = ClasseGap.Carrega(1)
# modifica a propriedade Descricao
classeGap.Descricao = "Descrição";
# salva modificação da propriedade Descricao
ClasseGap.Salva(classeGap)
```
