# PessoaId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorPesquisa > PessoaId

Identificador da Pessoa associada

**Exemplo 1: modificação da propriedade PessoaId**

```
# carrega objeto ApuracaoIndicadorPesquisa de identificador 1
apuracaoIndicadorPesquisa = ApuracaoIndicadorPesquisa.Carrega(1)
# modifica a propriedade PessoaId
apuracaoIndicadorPesquisa.PessoaId = 1;
# salva modificação da propriedade PessoaId
ApuracaoIndicadorPesquisa.Salva(apuracaoIndicadorPesquisa)
```
