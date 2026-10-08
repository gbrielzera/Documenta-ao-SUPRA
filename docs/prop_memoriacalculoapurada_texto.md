# Propriedade Texto

Caminho: Propriedade Texto

Texto gerado pela rotina de Apuração de Indicadores. Este texto pode ser utilizado pelo usuário para conferências nos números gerados pela Apuração.

**Exemplo 1: modificação da propriedade Texto**

```
# carrega objeto MemoriaCalculoApurada de identificador 1
memoriaCalculoApurada = MemoriaCalculoApurada.Carrega(1)
# modifica a propriedade Texto
memoriaCalculoApurada.Texto = "Texto";
# salva modificação da propriedade Texto
MemoriaCalculoApurada.Salva(memoriaCalculoApurada)
```
