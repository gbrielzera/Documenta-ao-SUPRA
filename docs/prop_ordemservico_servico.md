# Servico

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Servico

Serviço prestado pela Ocorrência de Processo.

**Exemplo 1: modificação da propriedade Servico**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade Servico
ordemServico.Servico = Servico.Carrega(23);
# salva modificação da propriedade Servico
OrdemServico.Salva(ordemServico)
```
