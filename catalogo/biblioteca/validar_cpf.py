# validar_cpf
# Caminho: Catálogo > Biblioteca de scripts > validar_cpf
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import re
def validar_cpf(cpf):
  # Remove special characters and spaces
  cpf = "".join(cpf.split())
  # Check length
  if len(cpf) != 11:
    return False
  # Calculate verification digits
  digits = [int(d) for d in cpf[:9]]
  
  sum1 = sum(d * (10-i) for i, d in enumerate(digits))
  mod1 = sum1 % 11
  verification_digit1 = 0 if mod1 < 2 else 11 - mod1
  
  digits.append(verification_digit1)
  sum2 = sum(d * (11-i) for i, d in enumerate(digits))
  mod2 = sum2 % 11
  verification_digit2 = 0 if mod2 < 2 else 11 - mod2
  # Check if verification digits match
  return cpf[-2:] == str(verification_digit1) + str(verification_digit2)
