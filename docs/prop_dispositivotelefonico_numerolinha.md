# NumeroLinha

Caminho: Customização > Modelo de objetos > Ativos > DispositivoTelefonico > NumeroLinha

Número de linha

**Exemplo 1: modificação da propriedade NumeroLinha**

```
# carrega objeto DispositivoTelefonico de identificador 1
dispositivoTelefonico = DispositivoTelefonico.Carrega(1)
# modifica a propriedade NumeroLinha
dispositivoTelefonico.NumeroLinha = "Número linha";
# salva modificação da propriedade NumeroLinha
DispositivoTelefonico.Salva(dispositivoTelefonico)
```
