# Descricao

Caminho: Customização > Modelo de objetos > Ativos > Modelo > Descricao

Descrição detalhada sobre o Modelo

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Modelo de identificador 1
modelo = Modelo.Carrega(1)
# modifica a propriedade Descricao
modelo.Descricao = "Latitude D610";
# salva modificação da propriedade Descricao
Modelo.Salva(modelo)
```
