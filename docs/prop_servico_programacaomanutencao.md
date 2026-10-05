# ProgramacaoManutencao

Caminho: Customização > Modelo de objetos > Processo > Servico > ProgramacaoManutencao

Detalhes sobre a Programação de Manutenção do Serviço incluíndo janelas semanais de paradas.

**Exemplo 1: modificação da propriedade ProgramacaoManutencao**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade ProgramacaoManutencao
servico.ProgramacaoManutencao = "Programação manutenção";
# salva modificação da propriedade ProgramacaoManutencao
Servico.Salva(servico)
```
