# HardwareAutoAtendimento

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > HardwareAutoAtendimento

Computador identificado pela aplicação de Autoatendimento no instante da abertura do chamado

**Exemplo 1: modificação da propriedade HardwareAutoAtendimento**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade HardwareAutoAtendimento
ordemServico.HardwareAutoAtendimento = "Computador Autoatendimento";
# salva modificação da propriedade HardwareAutoAtendimento
OrdemServico.Salva(ordemServico)
```
