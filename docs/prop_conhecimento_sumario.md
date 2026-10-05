# Sumario

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento > Sumario

Sumário

**Exemplo 1: modificação da propriedade Sumario**

```
# carrega objeto Conhecimento de identificador 1
conhecimento = Conhecimento.Carrega(1)
# modifica a propriedade Sumario
conhecimento.Sumario = "Sumário";
# salva modificação da propriedade Sumario
Conhecimento.Salva(conhecimento)
```
