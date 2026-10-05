# PlanoGestao

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > PlanoGestao

O Plano de Gestão é utilizado para gerenciar Indicadores de Desempenho. Este plano pode ser utilizado para gestão de Indicadores de Desempenho Chave da área ou indicadores associados a Acordos de Nível de Serviço.

**Exemplo 1: modificação da propriedade PlanoGestao**

```
# carrega objeto ApuracaoIndicador de identificador 78
apuracaoIndicador = ApuracaoIndicador.Carrega(78)
# modifica a propriedade PlanoGestao
apuracaoIndicador.PlanoGestao = PlanoGestao.Carrega(23);
# salva modificação da propriedade PlanoGestao
ApuracaoIndicador.Salva(apuracaoIndicador)
```
