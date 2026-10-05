# DescricaoCliente

Caminho: Customização > Modelo de objetos > Processo > MacroProcesso > DescricaoCliente

Descritivo apresentado para o cliente no passo de seleção de macro-processos da função de Abertura de Ordens de Serviço do Autoatendimento. Se não for informado então o sistema utilizará o próprio descritivo do macro-processo.

**Exemplo 1: modificação da propriedade DescricaoCliente**

```
# carrega objeto MacroProcesso de identificador 1
macroProcesso = MacroProcesso.Carrega(1)
# modifica a propriedade DescricaoCliente
macroProcesso.DescricaoCliente = "Descrição para clientes";
# salva modificação da propriedade DescricaoCliente
MacroProcesso.Salva(macroProcesso)
```
