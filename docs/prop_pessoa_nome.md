# Nome

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Nome

Nome completo da Pessoa

**Exemplo 1: modificação da propriedade Nome**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Nome
pessoa.Nome = "José Aparecido Santos Silva";
# salva modificação da propriedade Nome
Pessoa.Salva(pessoa)
```
