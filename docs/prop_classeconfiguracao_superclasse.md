# SuperClasse

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > SuperClasse

Nome do Super Tipo associado que pode ser ser um Equipamento, Software, Dispositivo telefônico, Artigo da Base de Conhecimento ou Artefato (tipo genérico). Para cada Super tipo existe uma tela de cadastro no módulo de Ativos.

**Exemplo 1: modificação da propriedade SuperClasse**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade SuperClasse
classeConfiguracao.SuperClasse = "Hardware";
# salva modificação da propriedade SuperClasse
ClasseConfiguracao.Salva(classeConfiguracao)
```
