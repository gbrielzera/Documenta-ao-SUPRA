# TelefoneSegundoContato

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > TelefoneSegundoContato

Telefone do Segundo contato

**Exemplo 1: modificação da propriedade TelefoneSegundoContato**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade TelefoneSegundoContato
ordemServico.TelefoneSegundoContato = "Telefone Segundo contato";
# salva modificação da propriedade TelefoneSegundoContato
OrdemServico.Salva(ordemServico)
```
