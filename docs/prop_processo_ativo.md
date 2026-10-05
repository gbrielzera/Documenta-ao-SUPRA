# Ativo

Caminho: Customização > Modelo de objetos > Processo > Processo > Ativo

Indica que o Tipo de Serviço está Ativo. Quando ativo o Tipo é visível em formulários de entrada de dados para Ordens de Serviço ou Consultas diversas

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade Ativo
processo.Ativo = true;
# salva modificação da propriedade Ativo
Processo.Salva(processo)
```
