# PermiteMotivoDigitado

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > PermiteMotivoDigitado

Permite a informação do Motivo do Apontamento por digitação e não por seleção de Item mantido na propriedade Motivos.

**Exemplo 1: modificação da propriedade PermiteMotivoDigitado**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade PermiteMotivoDigitado
classeApontamento.PermiteMotivoDigitado = true;
# salva modificação da propriedade PermiteMotivoDigitado
ClasseApontamento.Salva(classeApontamento)
```
