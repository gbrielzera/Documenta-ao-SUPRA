# PlanoGestao

Caminho: Customização > Modelo de objetos > Recurso > Contrato > PlanoGestao

Indicadores de Desempenho para Gestão do Contrato

**Exemplo 1: modificação da propriedade PlanoGestao**

```
# carrega objeto Contrato de identificador 51
contrato = Contrato.Carrega(51)
# modifica a propriedade PlanoGestao
contrato.PlanoGestao = PlanoGestao.Carrega(94);
# salva modificação da propriedade PlanoGestao
Contrato.Salva(contrato)
```
