# ResponsavelId

Caminho: Customização > Modelo de objetos > Processo > Apontamento > ResponsavelId

Identificador do Responsável pelo Apontamento

**Exemplo 1: modificação da propriedade ResponsavelId**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade ResponsavelId
apontamento.ResponsavelId = 1;
# salva modificação da propriedade ResponsavelId
Apontamento.Salva(apontamento)
```
