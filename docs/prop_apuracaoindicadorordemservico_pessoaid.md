# PessoaId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorOrdemServico > PessoaId

Identificador da Pessoa associada

**Exemplo 1: modificação da propriedade PessoaId**

```
# carrega objeto ApuracaoIndicadorOrdemServico de identificador 1
apuracaoIndicadorOrdemServico = ApuracaoIndicadorOrdemServico.Carrega(1)
# modifica a propriedade PessoaId
apuracaoIndicadorOrdemServico.PessoaId = 1;
# salva modificação da propriedade PessoaId
ApuracaoIndicadorOrdemServico.Salva(apuracaoIndicadorOrdemServico)
```
