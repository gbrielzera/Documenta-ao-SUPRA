# Id

Caminho: Customização > Modelo de objetos > Recurso > Calendario > Id

Número seqüencial gerado por sistema para identificação de um Calendário

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Calendario de identificador 1
calendario = Calendario.Carrega(1)
# modifica a propriedade Id
calendario.Id = 1;
# salva modificação da propriedade Id
Calendario.Salva(calendario)
```
