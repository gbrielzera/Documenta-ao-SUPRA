# CorIndicadorGrafico

Caminho: Customização > Modelo de objetos > Processo > NivelSLA > CorIndicadorGrafico

Cor associada ao nível de ANS. Na tela da de Fila de Ordens de Serviço é exibido um ícone nesta cor indicando o Nível atual de ANS.

**Exemplo 1: modificação da propriedade CorIndicadorGrafico**

```
# carrega objeto NivelSLA de identificador 1
nivelSLA = NivelSLA.Carrega(1)
# modifica a propriedade CorIndicadorGrafico
nivelSLA.CorIndicadorGrafico = "Verde";
# salva modificação da propriedade CorIndicadorGrafico
NivelSLA.Salva(nivelSLA)
```
