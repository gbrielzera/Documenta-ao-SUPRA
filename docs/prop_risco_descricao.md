# Descricao

Caminho: Customização > Modelo de objetos > Processo > Risco > Descricao

Descrição detalhada do Risco

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Risco de identificador 1
risco = Risco.Carrega(1)
# modifica a propriedade Descricao
risco.Descricao = "Descrição";
# salva modificação da propriedade Descricao
Risco.Salva(risco)
```
