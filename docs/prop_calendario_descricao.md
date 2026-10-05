# Descricao

Caminho: Customização > Modelo de objetos > Recurso > Calendario > Descricao

Texto que descreve claramente o conteúdo e a aplicação de um Calendário.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Calendario de identificador 1
calendario = Calendario.Carrega(1)
# modifica a propriedade Descricao
calendario.Descricao = "Descrição";
# salva modificação da propriedade Descricao
Calendario.Salva(calendario)
```
