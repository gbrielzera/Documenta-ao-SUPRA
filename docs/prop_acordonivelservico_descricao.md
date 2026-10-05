# Descricao

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > Descricao

Texto que descreve claramente a aplicação do Acordo de Nível de Serviço. Recomenda-se incluir o período de vigência e, quando possível, área atendida pelo Acordo.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade Descricao
acordoNivelServico.Descricao = "Acordo Geral 2009";
# salva modificação da propriedade Descricao
AcordoNivelServico.Salva(acordoNivelServico)
```
