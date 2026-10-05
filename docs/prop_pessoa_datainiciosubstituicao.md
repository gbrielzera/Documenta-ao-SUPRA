# DataInicioSubstituicao

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > DataInicioSubstituicao

Data de Início de validade para a autorização de substituição. Importante: a data de início não está associada a data de início de aprovação (instante em que soliictação de aprovação é enviada para o aprovador) e sim com a data instantânea em que a página de aprovação é exibida para o Cliente.

**Exemplo 1: modificação da propriedade DataInicioSubstituicao**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade DataInicioSubstituicao
pessoa.DataInicioSubstituicao = DateTime;
# salva modificação da propriedade DataInicioSubstituicao
Pessoa.Salva(pessoa)
```
