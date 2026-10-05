# ResponsavelArea

Caminho: Customização > Modelo de objetos > Processo > Servico > ResponsavelArea

Gerência responsável pelo Serviço na área de negócio cliente do Serviço

**Exemplo 1: modificação da propriedade ResponsavelArea**

```
# carrega objeto Servico de identificador 78
servico = Servico.Carrega(78)
# modifica a propriedade ResponsavelArea
servico.ResponsavelArea = Pessoa.Carrega(23);
# salva modificação da propriedade ResponsavelArea
Servico.Salva(servico)
```
