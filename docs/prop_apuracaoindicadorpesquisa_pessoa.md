# Pessoa

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorPesquisa > Pessoa

Pessoa avaliada pela Pesquisa

**Exemplo 1: modificação da propriedade Pessoa**

```
# carrega objeto ApuracaoIndicadorPesquisa de identificador 94
apuracaoIndicadorPesquisa = ApuracaoIndicadorPesquisa.Carrega(94)
# modifica a propriedade Pessoa
apuracaoIndicadorPesquisa.Pessoa = Pessoa.Carrega(82);
# salva modificação da propriedade Pessoa
ApuracaoIndicadorPesquisa.Salva(apuracaoIndicadorPesquisa)
```
