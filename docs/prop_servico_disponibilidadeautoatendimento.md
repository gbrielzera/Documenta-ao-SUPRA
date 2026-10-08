# Propriedade DisponibilidadeAutoAtendimento

Caminho: Propriedade DisponibilidadeAutoAtendimento

Configuração da disponibilidade do Serviço na aplicação de Auto-atendimento. Alguns Serviços são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente.

**Exemplo 1: modificação da propriedade DisponibilidadeAutoAtendimento**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade DisponibilidadeAutoAtendimento
servico.DisponibilidadeAutoAtendimento = "Nunca";
# salva modificação da propriedade DisponibilidadeAutoAtendimento
Servico.Salva(servico)
```
