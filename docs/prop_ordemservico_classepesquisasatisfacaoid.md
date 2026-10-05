# ClassePesquisaSatisfacaoId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ClassePesquisaSatisfacaoId

Identificador do ClassePesquisaSatisfacao associado

**Exemplo 1: modificação da propriedade ClassePesquisaSatisfacaoId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ClassePesquisaSatisfacaoId
ordemServico.ClassePesquisaSatisfacaoId = 1;
# salva modificação da propriedade ClassePesquisaSatisfacaoId
OrdemServico.Salva(ordemServico)
```
