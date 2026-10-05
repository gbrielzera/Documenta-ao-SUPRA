# SumarioTexto

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento > SumarioTexto

Sumário em forma de texto, sem as TAGs html

**Exemplo 1: modificação da propriedade SumarioTexto**

```
# carrega objeto Conhecimento de identificador 1
conhecimento = Conhecimento.Carrega(1)
# modifica a propriedade SumarioTexto
conhecimento.SumarioTexto = "Sumário";
# salva modificação da propriedade SumarioTexto
Conhecimento.Salva(conhecimento)
```
