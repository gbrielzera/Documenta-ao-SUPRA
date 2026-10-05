# Sequencial

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > Sequencial

Sequencial do apontamento em uma Ordem de Serviço

**Exemplo 1: modificação da propriedade Sequencial**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade Sequencial
timeSheet.Sequencial = 1;
# salva modificação da propriedade Sequencial
TimeSheet.Salva(timeSheet)
```
