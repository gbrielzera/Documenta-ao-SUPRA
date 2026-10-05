# Objeto Utils

Caminho: Recursos Avançados > Objeto Utils

O objeto Utils é um utilitário contendo funções utilizadas em scripts Python. Através destas funções é possível realizar ações como gravar eventos no log, acessar a envio de e-mail pelo Supravizio.

Este objeto possui os seguintes métodos:

**Funções:**

| **Nome** | **Descrição** |
|---|---|
| **LogError**(string message, string category) | Escreve uma mensagem do tipo Erro no mecanismo de log. O parâmetro category define o agrupamento a qual pertencerá a mensagem de Log. |
| **LogInformation**(string message, string category) | Escreve uma mensagem do tipo Informação no mecanismo de log. O parâmetro category define o agrupamento a qual pertencerá a mensagem de Log. |
| **LogWarning**(string message, string category) | Escreve uma mensagem do tipo Aviso no mecanismo de log. O parâmetro category define o agrupamento a qual pertencerá a mensagem de Log. |
| **SendMail**(string from, string to, string subject, string body) | Envia um email utilizando o mecanismo de envio de comunicados do produto. |
| **SendMail**(string from, string to, string subject, string body, string recoveryCode) | Envia um email utilizando o mecanismo de envio de comunicados do produto. |
| **IF**(bool testExpression, object ifValue, elseValue) | Avalia a expressão booleana do primeiro parâmetro. Se o resultado for verdadeiro então retorna o parâmetro ifValue e se for falso retorna o valor elseValue. |
