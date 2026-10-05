# EmailsComunicadosManuais

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > EmailsComunicadosManuais

Serão enviados para este(s) email(s) os emails enviados manualmente relacionados com este Tipo de Subprocesso. Separar por ponto-e-vírgula (;).

**Exemplo 1: modificação da propriedade EmailsComunicadosManuais**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade EmailsComunicadosManuais
classeSubProcesso.EmailsComunicadosManuais = "Emails para cópia em comunicado manual";
# salva modificação da propriedade EmailsComunicadosManuais
ClasseSubProcesso.Salva(classeSubProcesso)
```
