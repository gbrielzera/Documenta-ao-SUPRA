# ReaberturaAutoAtendimento

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > ReaberturaAutoAtendimento

Permite que clientes reabram a Ordem de Serviço utilizando a página de consulta do Autoatendimento. Esta permissão também está condicionada ao parâmetro 'Máximo dias para reabertura' da tela de Configurações.

**Exemplo 1: modificação da propriedade ReaberturaAutoAtendimento**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade ReaberturaAutoAtendimento
classeSubProcesso.ReaberturaAutoAtendimento = true;
# salva modificação da propriedade ReaberturaAutoAtendimento
ClasseSubProcesso.Salva(classeSubProcesso)
```
