# Disponibilidade

Caminho: Customização > Modelo de objetos > Processo > Servico > Disponibilidade

Disponibilidade que pode ser esperada pelo Cliente incluindo horários.

**Exemplo 1: modificação da propriedade Disponibilidade**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade Disponibilidade
servico.Disponibilidade = "Disponibilidade";
# salva modificação da propriedade Disponibilidade
Servico.Salva(servico)
```
