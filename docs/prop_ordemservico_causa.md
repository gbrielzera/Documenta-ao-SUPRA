# Causa

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Causa

Causa

**Exemplo 1: modificação da propriedade Causa**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade Causa
ordemServico.Causa = "Causa";
# salva modificação da propriedade Causa
OrdemServico.Salva(ordemServico)
```
