# ServicoId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorPesquisa > ServicoId

Identificador do Servico associado

**Exemplo 1: modificação da propriedade ServicoId**

```
# carrega objeto ApuracaoIndicadorPesquisa de identificador 1
apuracaoIndicadorPesquisa = ApuracaoIndicadorPesquisa.Carrega(1)
# modifica a propriedade ServicoId
apuracaoIndicadorPesquisa.ServicoId = 1;
# salva modificação da propriedade ServicoId
ApuracaoIndicadorPesquisa.Salva(apuracaoIndicadorPesquisa)
```
