# Justificativa

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Justificativa

Justificativa fornecida pelo Cliente para atendimento do Serviço

**Exemplo 1: modificação da propriedade Justificativa**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade Justificativa
ordemServico.Justificativa = "Justificativa";
# salva modificação da propriedade Justificativa
OrdemServico.Salva(ordemServico)
```
