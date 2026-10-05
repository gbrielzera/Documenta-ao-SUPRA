# Sigla

Caminho: Customização > Modelo de objetos > Processo > ClasseServico > Sigla

Nome resumido (código) que identifica unicamente um Tipo de Item de Configuração

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto ClasseServico de identificador 1
classeServico = ClasseServico.Carrega(1)
# modifica a propriedade Sigla
classeServico.Sigla = "INFRA";
# salva modificação da propriedade Sigla
ClasseServico.Salva(classeServico)
```
