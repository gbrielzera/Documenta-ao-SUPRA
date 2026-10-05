# PublicaInformacoesAA

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > PublicaInformacoesAA

Permite publicar ou não informações sobre ANS no site de Autoatendimento. As informações são exibidas no Autoatendimento na página de consulta e na finalização de abertura de uma Ordem de Serviço.

**Exemplo 1: modificação da propriedade PublicaInformacoesAA**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade PublicaInformacoesAA
acordoNivelServico.PublicaInformacoesAA = true;
# salva modificação da propriedade PublicaInformacoesAA
AcordoNivelServico.Salva(acordoNivelServico)
```
