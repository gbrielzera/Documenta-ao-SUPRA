# Sequencial

Caminho: Customização > Modelo de objetos > Processo > NivelSLA > Sequencial

Sequencial

**Exemplo 1: modificação da propriedade Sequencial**

```
# carrega objeto NivelSLA de identificador 1
nivelSLA = NivelSLA.Carrega(1)
# modifica a propriedade Sequencial
nivelSLA.Sequencial = 1;
# salva modificação da propriedade Sequencial
NivelSLA.Salva(nivelSLA)
```
