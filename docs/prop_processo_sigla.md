# Sigla

Caminho: Customização > Modelo de objetos > Processo > Processo > Sigla

Nome abreviado para o Processo. Este identificador pode ser utilizado por scripts para automatização de processos.

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade Sigla
processo.Sigla = "INCIDENTE";
# salva modificação da propriedade Sigla
Processo.Salva(processo)
```
