# TipoColaborador

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > TipoColaborador

Tipo de Colaborador que pode ser Empregado ou Terceiro. No caso de Terceiro é necessário informar a Empresa Fornecedora

**Exemplo 1: modificação da propriedade TipoColaborador**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade TipoColaborador
pessoa.TipoColaborador = "Empregado";
# salva modificação da propriedade TipoColaborador
Pessoa.Salva(pessoa)
```
