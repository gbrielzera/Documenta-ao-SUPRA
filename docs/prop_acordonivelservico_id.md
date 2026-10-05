# Id

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um AcordoNivelServico

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade Id
acordoNivelServico.Id = 1;
# salva modificação da propriedade Id
AcordoNivelServico.Salva(acordoNivelServico)
```
