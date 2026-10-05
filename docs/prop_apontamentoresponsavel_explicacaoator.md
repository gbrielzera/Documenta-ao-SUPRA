# ExplicacaoAtor

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > ExplicacaoAtor

Texto explicativo sobre o cálculo de um ator na Ordem de Serviço.

**Exemplo 1: modificação da propriedade ExplicacaoAtor**

```
# carrega objeto ApontamentoResponsavel de identificador 1
apontamentoResponsavel = ApontamentoResponsavel.Carrega(1)
# modifica a propriedade ExplicacaoAtor
apontamentoResponsavel.ExplicacaoAtor = "Explicação sobre ator";
# salva modificação da propriedade ExplicacaoAtor
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
