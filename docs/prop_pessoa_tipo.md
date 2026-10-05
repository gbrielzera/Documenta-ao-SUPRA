# Tipo

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Tipo

Cliente em Ordens de Serviço ou Fila de Grupos de Trabalho

**Exemplo 1: modificação da propriedade Tipo**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Tipo
pessoa.Tipo = "Cliente";
# salva modificação da propriedade Tipo
Pessoa.Salva(pessoa)
```
