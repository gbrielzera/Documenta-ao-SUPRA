# CulturaCliente

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > CulturaCliente

Cultura preferencial do Cliente. Esta Cultura é utilizada pela aplicação de Autoatendimento para configuração de idioma do usuário.

**Exemplo 1: modificação da propriedade CulturaCliente**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade CulturaCliente
pessoa.CulturaCliente = Culture.Carrega(94);
# salva modificação da propriedade CulturaCliente
Pessoa.Salva(pessoa)
```
