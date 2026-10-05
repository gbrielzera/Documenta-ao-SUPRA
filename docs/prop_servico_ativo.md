# Ativo

Caminho: Customização > Modelo de objetos > Processo > Servico > Ativo

Define se o Serviço está Ativo. Por padrão o valor inicial é sempre Verdadeiro.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade Ativo
servico.Ativo = true;
# salva modificação da propriedade Ativo
Servico.Salva(servico)
```
