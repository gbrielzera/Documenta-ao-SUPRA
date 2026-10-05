# SegundoContato

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > SegundoContato

Segunda pessoa para contato com o Solicitante da Ordem de Serviço

**Exemplo 1: modificação da propriedade SegundoContato**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade SegundoContato
ordemServico.SegundoContato = "Segundo contato";
# salva modificação da propriedade SegundoContato
OrdemServico.Salva(ordemServico)
```
