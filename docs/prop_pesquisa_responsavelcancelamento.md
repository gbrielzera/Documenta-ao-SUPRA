# ResponsavelCancelamento

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > ResponsavelCancelamento

Pessoa responsável pelo Cancelamento da Pesquisa de Satisfação

**Exemplo 1: modificação da propriedade ResponsavelCancelamento**

```
# carrega objeto Pesquisa de identificador 78
pesquisa = Pesquisa.Carrega(78)
# modifica a propriedade ResponsavelCancelamento
pesquisa.ResponsavelCancelamento = Pessoa.Carrega(23);
# salva modificação da propriedade ResponsavelCancelamento
Pesquisa.Salva(pesquisa)
```
