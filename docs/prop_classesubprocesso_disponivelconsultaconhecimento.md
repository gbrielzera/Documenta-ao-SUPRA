# DisponivelConsultaConhecimento

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > DisponivelConsultaConhecimento

Ordens de Serviço deste Subprocesso podem ser recuperadas pela ferramenta de busca de base de conhecimento.

**Exemplo 1: modificação da propriedade DisponivelConsultaConhecimento**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade DisponivelConsultaConhecimento
classeSubProcesso.DisponivelConsultaConhecimento = true;
# salva modificação da propriedade DisponivelConsultaConhecimento
ClasseSubProcesso.Salva(classeSubProcesso)
```
