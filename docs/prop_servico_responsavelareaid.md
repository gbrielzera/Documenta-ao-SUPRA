# ResponsavelAreaId

Caminho: Customização > Modelo de objetos > Processo > Servico > ResponsavelAreaId

Identificador da Pessoa responsável pela área de negócio cliente do Serviço

**Exemplo 1: modificação da propriedade ResponsavelAreaId**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade ResponsavelAreaId
servico.ResponsavelAreaId = 1;
# salva modificação da propriedade ResponsavelAreaId
Servico.Salva(servico)
```
