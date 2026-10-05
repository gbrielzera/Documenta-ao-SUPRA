# Sigla

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > Sigla

Nome abreviado (código) utilizado para recuperar um Tipo de Item de Configuração em comandos SQL de relatórios ou scripts de customização. Esta sigla deve contar apenas números e letras.

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade Sigla
classeConfiguracao.Sigla = "DESKTOP";
# salva modificação da propriedade Sigla
ClasseConfiguracao.Salva(classeConfiguracao)
```
