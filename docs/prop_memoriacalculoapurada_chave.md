# Propriedade Chave

Caminho: Propriedade Chave

Chave para recuperação do objeto apurado

**Exemplo 1: modificação da propriedade Chave**

```
# carrega objeto MemoriaCalculoApurada de identificador 1
memoriaCalculoApurada = MemoriaCalculoApurada.Carrega(1)
# modifica a propriedade Chave
memoriaCalculoApurada.Chave = "Chave";
# salva modificação da propriedade Chave
MemoriaCalculoApurada.Salva(memoriaCalculoApurada)
```
