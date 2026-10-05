# Id

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma ClassePesquisaSatisfacao

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 1
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(1)
# modifica a propriedade Id
classePesquisaSatisfacao.Id = 1;
# salva modificação da propriedade Id
ClassePesquisaSatisfacao.Salva(classePesquisaSatisfacao)
```
