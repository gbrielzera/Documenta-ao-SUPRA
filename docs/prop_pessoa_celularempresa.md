# CelularEmpresa

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > CelularEmpresa

Telefone Celular fornecido pela empresa

**Exemplo 1: modificação da propriedade CelularEmpresa**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade CelularEmpresa
pessoa.CelularEmpresa = "9189-9933";
# salva modificação da propriedade CelularEmpresa
Pessoa.Salva(pessoa)
```
