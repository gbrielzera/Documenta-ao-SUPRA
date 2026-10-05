# Descricao

Caminho: Customização > Modelo de objetos > Processo > Servico > Descricao

Descrição detalhada do Produto

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade Descricao
servico.Descricao = "Rede";
# salva modificação da propriedade Descricao
Servico.Salva(servico)
```
