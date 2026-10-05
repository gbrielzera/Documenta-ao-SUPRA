# Provedor

Caminho: Customização > Modelo de objetos > Processo > Indicador > Provedor

Banco de dados utilizado para apuração do Indicador.

**Exemplo 1: modificação da propriedade Provedor**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade Provedor
indicador.Provedor = "OrdemServico";
# salva modificação da propriedade Provedor
Indicador.Salva(indicador)
```
