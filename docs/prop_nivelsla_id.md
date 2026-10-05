# Id

Caminho: Customização > Modelo de objetos > Processo > NivelSLA > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um NivelSLA

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto NivelSLA de identificador 1
nivelSLA = NivelSLA.Carrega(1)
# modifica a propriedade Id
nivelSLA.Id = 1;
# salva modificação da propriedade Id
NivelSLA.Salva(nivelSLA)
```
