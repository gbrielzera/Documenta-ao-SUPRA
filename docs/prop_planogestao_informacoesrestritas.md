# InformacoesRestritas

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao > InformacoesRestritas

O solucionador logado só visualiza suas informações ou informações de subordinados.

**Exemplo 1: modificação da propriedade InformacoesRestritas**

```
# carrega objeto PlanoGestao de identificador 1
planoGestao = PlanoGestao.Carrega(1)
# modifica a propriedade InformacoesRestritas
planoGestao.InformacoesRestritas = true;
# salva modificação da propriedade InformacoesRestritas
PlanoGestao.Salva(planoGestao)
```
