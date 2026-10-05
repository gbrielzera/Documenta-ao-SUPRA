# DisponibilidadeAA

Caminho: Customização > Modelo de objetos > Processo > Servico > DisponibilidadeAA

Configuração da disponibilidade do Serviço na aplicação de Autoatendimento. Alguns Serviços são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente.

**Exemplo 1: modificação da propriedade DisponibilidadeAA**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade DisponibilidadeAA
servico.DisponibilidadeAA = true;
# salva modificação da propriedade DisponibilidadeAA
Servico.Salva(servico)
```
