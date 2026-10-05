# Pessoa

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorOrdemServico > Pessoa

Pessoa responsável pela Ordem de Serviço

**Exemplo 1: modificação da propriedade Pessoa**

```
# carrega objeto ApuracaoIndicadorOrdemServico de identificador 94
apuracaoIndicadorOrdemServico = ApuracaoIndicadorOrdemServico.Carrega(94)
# modifica a propriedade Pessoa
apuracaoIndicadorOrdemServico.Pessoa = Pessoa.Carrega(82);
# salva modificação da propriedade Pessoa
ApuracaoIndicadorOrdemServico.Salva(apuracaoIndicadorOrdemServico)
```
