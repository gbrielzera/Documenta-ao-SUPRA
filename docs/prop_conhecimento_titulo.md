# Titulo

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento > Titulo

Título

**Exemplo 1: modificação da propriedade Titulo**

```
# carrega objeto Conhecimento de identificador 1
conhecimento = Conhecimento.Carrega(1)
# modifica a propriedade Titulo
conhecimento.Titulo = "Título";
# salva modificação da propriedade Titulo
Conhecimento.Salva(conhecimento)
```
