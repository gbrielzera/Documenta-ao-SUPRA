# LeituraResponsavel

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > LeituraResponsavel

Indica que o responsável atual pela Ordem de Serviço leu o conteúdo da Ordem de Serviço (visualizou na tela de edição).

**Exemplo 1: modificação da propriedade LeituraResponsavel**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade LeituraResponsavel
ordemServico.LeituraResponsavel = true;
# salva modificação da propriedade LeituraResponsavel
OrdemServico.Salva(ordemServico)
```
