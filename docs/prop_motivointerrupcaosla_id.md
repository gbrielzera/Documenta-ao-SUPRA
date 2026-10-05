# Id

Caminho: Customização > Modelo de objetos > Recurso > MotivoInterrupcaoSLA > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Motivo de interrução de cronometragem de tempo de ANS

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto MotivoInterrupcaoSLA de identificador 1
motivoInterrupcaoSLA = MotivoInterrupcaoSLA.Carrega(1)
# modifica a propriedade Id
motivoInterrupcaoSLA.Id = 1;
# salva modificação da propriedade Id
MotivoInterrupcaoSLA.Salva(motivoInterrupcaoSLA)
```
