# ClasseServico

Caminho: Customização > Modelo de objetos > Processo > Servico > ClasseServico

Classificação do Serviço. Este atributo é utilizado pelo Cliente na aplicação de Autoatendimento

**Exemplo 1: modificação da propriedade ClasseServico**

```
# carrega objeto Servico de identificador 78
servico = Servico.Carrega(78)
# modifica a propriedade ClasseServico
servico.ClasseServico = ClasseServico.Carrega(23);
# salva modificação da propriedade ClasseServico
Servico.Salva(servico)
```
