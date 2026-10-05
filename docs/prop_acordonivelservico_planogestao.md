# PlanoGestao

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > PlanoGestao

Conjunto de Indicadores de Desempenho (meta e realizado) para gerenciar o cumprimento do Acordo de Nível de Serviço.

**Exemplo 1: modificação da propriedade PlanoGestao**

```
# carrega objeto AcordoNivelServico de identificador 51
acordoNivelServico = AcordoNivelServico.Carrega(51)
# modifica a propriedade PlanoGestao
acordoNivelServico.PlanoGestao = PlanoGestao.Carrega(94);
# salva modificação da propriedade PlanoGestao
AcordoNivelServico.Salva(acordoNivelServico)
```
