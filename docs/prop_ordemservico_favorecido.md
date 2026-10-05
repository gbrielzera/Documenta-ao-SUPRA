# Favorecido

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Favorecido

Pessoa

**Exemplo 1: modificação da propriedade Favorecido**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade Favorecido
ordemServico.Favorecido = Pessoa.Carrega(23);
# salva modificação da propriedade Favorecido
OrdemServico.Salva(ordemServico)
```
