# HabilitaRedefinicaoPapeis

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > HabilitaRedefinicaoPapeis

Habilita a redefinição de Papéis por Itens da Classe. Papéis possuem uma definição global de Atores que pode ser sobreposta por um Serviço. Este parâmetro indica que Itens de Configuração desta Classe podem acumular um segundo nível de redefinição de Papéis, que ainda está condicionada a parametrização do Serviço.

**Exemplo 1: modificação da propriedade HabilitaRedefinicaoPapeis**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade HabilitaRedefinicaoPapeis
classeConfiguracao.HabilitaRedefinicaoPapeis = true;
# salva modificação da propriedade HabilitaRedefinicaoPapeis
ClasseConfiguracao.Salva(classeConfiguracao)
```
