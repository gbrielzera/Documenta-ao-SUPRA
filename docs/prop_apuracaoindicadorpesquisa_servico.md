# Servico

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorPesquisa > Servico

Um Serviço pode ser definido como um sistema composto por Tecnologia, Facilidades, Processos e Pessoas que habilitam um processo de negócio.

**Exemplo 1: modificação da propriedade Servico**

```
# carrega objeto ApuracaoIndicadorPesquisa de identificador 94
apuracaoIndicadorPesquisa = ApuracaoIndicadorPesquisa.Carrega(94)
# modifica a propriedade Servico
apuracaoIndicadorPesquisa.Servico = Servico.Carrega(82);
# salva modificação da propriedade Servico
ApuracaoIndicadorPesquisa.Salva(apuracaoIndicadorPesquisa)
```
