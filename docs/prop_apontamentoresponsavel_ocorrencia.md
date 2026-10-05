# Ocorrencia

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > Ocorrencia

Ocorrências de Processos

**Exemplo 1: modificação da propriedade Ocorrencia**

```
# carrega objeto ApontamentoResponsavel de identificador 94
apontamentoResponsavel = ApontamentoResponsavel.Carrega(94)
# modifica a propriedade Ocorrencia
apontamentoResponsavel.Ocorrencia = Ocorrencia.Carrega(82);
# salva modificação da propriedade Ocorrencia
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
