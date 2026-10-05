# MetodoPriorizacao

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > MetodoPriorizacao

Método utilizado para Priorização da Ordem de Serviço

**Exemplo 1: modificação da propriedade MetodoPriorizacao**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade MetodoPriorizacao
ordemServico.MetodoPriorizacao = MetodoPriorizacao.Carrega(23);
# salva modificação da propriedade MetodoPriorizacao
OrdemServico.Salva(ordemServico)
```
