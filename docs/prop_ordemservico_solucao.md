# Solucao

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Solucao

Solução

**Exemplo 1: modificação da propriedade Solucao**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade Solucao
ordemServico.Solucao = "Solução";
# salva modificação da propriedade Solucao
OrdemServico.Salva(ordemServico)
```
