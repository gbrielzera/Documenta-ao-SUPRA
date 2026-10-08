# Propriedade AcessoPublicoAutoAtendimento

Caminho: Propriedade AcessoPublicoAutoAtendimento

Indica que ocorrências deste Sub-processo são públicas na consulta de Ordens de Serviço disponível no Auto-atendimento.

**Exemplo 1: modificação da propriedade AcessoPublicoAutoAtendimento**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade AcessoPublicoAutoAtendimento
classeSubProcesso.AcessoPublicoAutoAtendimento = true;
# salva modificação da propriedade AcessoPublicoAutoAtendimento
ClasseSubProcesso.Salva(classeSubProcesso)
```
