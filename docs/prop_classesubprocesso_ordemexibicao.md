# OrdemExibicao

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > OrdemExibicao

Ordem de exibição da Solicitação na página de Abertura de Ordens de Serviço da aplicação de Autoatendimento. Quando preenchido a Solicitação é exibida em um grupo denominado "Principais solicitações", caso contrário é agrupado em "Demais solicitações". Em caso de empate por ordenação deste campo então é adotado como segundo critério a ordenação alfabética por Descritivo do Cliente

**Exemplo 1: modificação da propriedade OrdemExibicao**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade OrdemExibicao
classeSubProcesso.OrdemExibicao = 1;
# salva modificação da propriedade OrdemExibicao
ClasseSubProcesso.Salva(classeSubProcesso)
```
