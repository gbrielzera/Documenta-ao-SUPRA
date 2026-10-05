# Sequencial

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > Sequencial

Sequencial de responsabilidade para uma determinada Ordem de Serviço.

**Exemplo 1: modificação da propriedade Sequencial**

```
# carrega objeto ApontamentoResponsavel de identificador 1
apontamentoResponsavel = ApontamentoResponsavel.Carrega(1)
# modifica a propriedade Sequencial
apontamentoResponsavel.Sequencial = 1;
# salva modificação da propriedade Sequencial
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
