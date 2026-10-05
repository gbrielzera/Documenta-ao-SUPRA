# Id

Caminho: Customização > Modelo de objetos > Processo > Diagrama > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Diagrama

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Diagrama de identificador 1
diagrama = Diagrama.Carrega(1)
# modifica a propriedade Id
diagrama.Id = 1;
# salva modificação da propriedade Id
Diagrama.Salva(diagrama)
```
