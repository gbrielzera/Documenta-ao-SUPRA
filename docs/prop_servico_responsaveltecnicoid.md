# ResponsavelTecnicoId

Caminho: Customização > Modelo de objetos > Processo > Servico > ResponsavelTecnicoId

Identificador do Solucionador responsável

**Exemplo 1: modificação da propriedade ResponsavelTecnicoId**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade ResponsavelTecnicoId
servico.ResponsavelTecnicoId = 1;
# salva modificação da propriedade ResponsavelTecnicoId
Servico.Salva(servico)
```
