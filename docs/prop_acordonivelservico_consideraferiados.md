# ConsideraFeriados

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > ConsideraFeriados

Indica que todos os feriados do calendário associado com o Cliente são desconsiderados no cálculo de tempo (o intervalo referente ao feriado é excluído da contagem de tempo). Para consultar o calendário do cliente acesse o cadastro da Unidade onde está localizado o cliente (campo Local no cadastro da Pessoa).

**Exemplo 1: modificação da propriedade ConsideraFeriados**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade ConsideraFeriados
acordoNivelServico.ConsideraFeriados = true;
# salva modificação da propriedade ConsideraFeriados
AcordoNivelServico.Salva(acordoNivelServico)
```
