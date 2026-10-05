# Id

Caminho: Customização > Modelo de objetos > Processo > Servico > Id

Identificador do Serviço

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade Id
servico.Id = 1;
# salva modificação da propriedade Id
Servico.Salva(servico)
```
