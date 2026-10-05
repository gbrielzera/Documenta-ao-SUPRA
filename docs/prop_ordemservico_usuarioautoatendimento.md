# UsuarioAutoAtendimento

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > UsuarioAutoAtendimento

Usuário reconhecido pela aplicação de Autoatendimento. Este campo só é preenchido quando a Ordem de Serviço é aberta na aplicação de Autoatendimento.

**Exemplo 1: modificação da propriedade UsuarioAutoAtendimento**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade UsuarioAutoAtendimento
ordemServico.UsuarioAutoAtendimento = "Usuário logado no Autoatendimento";
# salva modificação da propriedade UsuarioAutoAtendimento
OrdemServico.Salva(ordemServico)
```
