# Orgao

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Orgao

Órgão onde a Pessoa está lotada. A lotação é de grande importância em processos que envolvem aprovações de chefias e hierárquica.

**Exemplo 1: modificação da propriedade Orgao**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade Orgao
pessoa.Orgao = Orgao.Carrega(94);
# salva modificação da propriedade Orgao
Pessoa.Salva(pessoa)
```
