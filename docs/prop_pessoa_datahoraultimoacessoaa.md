# DataHoraUltimoAcessoAA

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > DataHoraUltimoAcessoAA

Data/hora do último acesso ao Autoatendimento.

**Exemplo 1: modificação da propriedade DataHoraUltimoAcessoAA**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade DataHoraUltimoAcessoAA
pessoa.DataHoraUltimoAcessoAA = DateTime;
# salva modificação da propriedade DataHoraUltimoAcessoAA
Pessoa.Salva(pessoa)
```
