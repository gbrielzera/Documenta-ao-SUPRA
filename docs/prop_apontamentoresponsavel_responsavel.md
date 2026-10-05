# Responsavel

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > Responsavel

Pessoa que recebeu a ocorrência em sua fila (Destinatário do encaminhamento).

**Exemplo 1: modificação da propriedade Responsavel**

```
# carrega objeto ApontamentoResponsavel de identificador 94
apontamentoResponsavel = ApontamentoResponsavel.Carrega(94)
# modifica a propriedade Responsavel
apontamentoResponsavel.Responsavel = Pessoa.Carrega(82);
# salva modificação da propriedade Responsavel
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
