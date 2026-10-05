# NivelSLA

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > NivelSLA

Nível de ANS define faixas de tempo para escalonamento de ANS em um Método de Priorização (por exemplo Incidentes).

**Exemplo 1: modificação da propriedade NivelSLA**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade NivelSLA
ordemServico.NivelSLA = NivelSLA.Carrega(23);
# salva modificação da propriedade NivelSLA
OrdemServico.Salva(ordemServico)
```
