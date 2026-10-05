# Descricao

Caminho: Customização > Modelo de objetos > Recurso > MotivoInterrupcaoSLA > Descricao

Descrição detalhada do Motivo de interrupção de ANS

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto MotivoInterrupcaoSLA de identificador 1
motivoInterrupcaoSLA = MotivoInterrupcaoSLA.Carrega(1)
# modifica a propriedade Descricao
motivoInterrupcaoSLA.Descricao = "Descrição";
# salva modificação da propriedade Descricao
MotivoInterrupcaoSLA.Salva(motivoInterrupcaoSLA)
```
