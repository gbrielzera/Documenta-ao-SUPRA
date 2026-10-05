# ClasseServicoId

Caminho: Customização > Modelo de objetos > Processo > Servico > ClasseServicoId

Identificador do tipo de Serviço associado

**Exemplo 1: modificação da propriedade ClasseServicoId**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade ClasseServicoId
servico.ClasseServicoId = 1;
# salva modificação da propriedade ClasseServicoId
Servico.Salva(servico)
```
