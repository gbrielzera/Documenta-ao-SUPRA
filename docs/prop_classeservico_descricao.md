# Descricao

Caminho: Customização > Modelo de objetos > Processo > ClasseServico > Descricao

Descrição detalhada do Tipo de Serviço

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ClasseServico de identificador 1
classeServico = ClasseServico.Carrega(1)
# modifica a propriedade Descricao
classeServico.Descricao = "Infra-estrutura";
# salva modificação da propriedade Descricao
ClasseServico.Salva(classeServico)
```
