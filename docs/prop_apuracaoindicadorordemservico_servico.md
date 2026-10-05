# Servico

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorOrdemServico > Servico

Um Serviço pode ser definido como um sistema composto por Tecnologia, Facilidades, Processos e Pessoas que habilitam um processo de negócio.

**Exemplo 1: modificação da propriedade Servico**

```
# carrega objeto ApuracaoIndicadorOrdemServico de identificador 94
apuracaoIndicadorOrdemServico = ApuracaoIndicadorOrdemServico.Carrega(94)
# modifica a propriedade Servico
apuracaoIndicadorOrdemServico.Servico = Servico.Carrega(82);
# salva modificação da propriedade Servico
ApuracaoIndicadorOrdemServico.Salva(apuracaoIndicadorOrdemServico)
```
