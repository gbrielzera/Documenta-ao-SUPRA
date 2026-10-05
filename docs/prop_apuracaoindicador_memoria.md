# Memoria

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > Memoria

Memória de cálculo com as chaves e valores. Formato: {IdObjeto}{S=atendeu critério;N=não atendeu critério}, ex: 1028S (Id igual 1028 e atendeu critério)

**Exemplo 1: modificação da propriedade Memoria**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade Memoria
# salva modificação da propriedade Memoria
ApuracaoIndicador.Salva(apuracaoIndicador)
```
