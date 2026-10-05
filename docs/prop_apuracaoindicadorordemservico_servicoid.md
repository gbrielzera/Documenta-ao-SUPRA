# ServicoId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorOrdemServico > ServicoId

Identificador do Servico associado

**Exemplo 1: modificação da propriedade ServicoId**

```
# carrega objeto ApuracaoIndicadorOrdemServico de identificador 1
apuracaoIndicadorOrdemServico = ApuracaoIndicadorOrdemServico.Carrega(1)
# modifica a propriedade ServicoId
apuracaoIndicadorOrdemServico.ServicoId = 1;
# salva modificação da propriedade ServicoId
ApuracaoIndicadorOrdemServico.Salva(apuracaoIndicadorOrdemServico)
```
