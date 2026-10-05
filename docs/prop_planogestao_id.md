# Id

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um PlanoGestao

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto PlanoGestao de identificador 1
planoGestao = PlanoGestao.Carrega(1)
# modifica a propriedade Id
planoGestao.Id = 1;
# salva modificação da propriedade Id
PlanoGestao.Salva(planoGestao)
```
