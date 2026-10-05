# Cargo

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Cargo

Descrição do Cargo da Pessoa

**Exemplo 1: modificação da propriedade Cargo**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Cargo
pessoa.Cargo = "Analista de Sistemas";
# salva modificação da propriedade Cargo
Pessoa.Salva(pessoa)
```
