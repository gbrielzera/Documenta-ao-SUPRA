# Propriedade LocalAtendimento

Caminho: Propriedade LocalAtendimento

Local de atendimento da Ordem de Serviço que, por default, é o mesmo do Cliente.

**Exemplo 1: modificação da propriedade LocalAtendimento**

```
# carrega objeto OrdemServico de identificador 85
ordemServico = OrdemServico.Carrega(85)
# modifica a propriedade LocalAtendimento
ordemServico.LocalAtendimento = Local.Carrega(73);
# salva modificação da propriedade LocalAtendimento
OrdemServico.Salva(ordemServico)
```
