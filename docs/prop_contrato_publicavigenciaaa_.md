# PublicaVigenciaAA

Caminho: Customização > Modelo de objetos > Recurso > Contrato > PublicaVigenciaAA

Publicar a vigência do contrato (data de início e fim de validade) na página de contratos do Autoatendimento

**Exemplo 1: modificação da propriedade PublicaVigenciaAA**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade PublicaVigenciaAA
contrato.PublicaVigenciaAA = true;
# salva modificação da propriedade PublicaVigenciaAA
Contrato.Salva(contrato)
```
