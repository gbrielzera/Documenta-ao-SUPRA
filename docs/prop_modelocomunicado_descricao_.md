# Descricao

Caminho: Customização > Modelo de objetos > Processo > ModeloComunicado > Descricao

Descrição detalhada do ModeloComunicado

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ModeloComunicado de identificador 1
modeloComunicado = ModeloComunicado.Carrega(1)
# modifica a propriedade Descricao
modeloComunicado.Descricao = "Descrição";
# salva modificação da propriedade Descricao
ModeloComunicado.Salva(modeloComunicado)
```
