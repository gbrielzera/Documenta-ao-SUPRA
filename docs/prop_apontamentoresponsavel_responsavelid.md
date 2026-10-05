# ResponsavelId

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > ResponsavelId

Identificador do Solucionador Responsável

**Exemplo 1: modificação da propriedade ResponsavelId**

```
# carrega objeto ApontamentoResponsavel de identificador 1
apontamentoResponsavel = ApontamentoResponsavel.Carrega(1)
# modifica a propriedade ResponsavelId
apontamentoResponsavel.ResponsavelId = 1;
# salva modificação da propriedade ResponsavelId
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
