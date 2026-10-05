# Referencia

Caminho: Customização > Modelo de objetos > Processo > Apropriacao > Referencia

Referência da Apropriação

**Exemplo 1: modificação da propriedade Referencia**

```
# carrega objeto Apropriacao de identificador 1
apropriacao = Apropriacao.Carrega(1)
# modifica a propriedade Referencia
apropriacao.Referencia = "Referência";
# salva modificação da propriedade Referencia
Apropriacao.Salva(apropriacao)
```
