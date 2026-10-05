# ResponsavelTecnico

Caminho: Customização > Modelo de objetos > Processo > Servico > ResponsavelTecnico

Solucionador responsável pelo Serviço

**Exemplo 1: modificação da propriedade ResponsavelTecnico**

```
# carrega objeto Servico de identificador 78
servico = Servico.Carrega(78)
# modifica a propriedade ResponsavelTecnico
servico.ResponsavelTecnico = Pessoa.Carrega(23);
# salva modificação da propriedade ResponsavelTecnico
Servico.Salva(servico)
```
