# SegundoContato

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > SegundoContato

Segunda Pessoa para contato

**Exemplo 1: modificação da propriedade SegundoContato**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade SegundoContato
pessoa.SegundoContato = "José Dornelas";
# salva modificação da propriedade SegundoContato
Pessoa.Salva(pessoa)
```
