print("Hi... World?\n\n")

# Modulo do Python para gerar numeros aleatorios
import random
print("----- Jogo de Adivinhação -----\n")
print("Adivinhe o número secreto")

# 'randint' gera um numero aleatorio inteiro
number_secret = random.randint(0, 50)
chute = input("Chute o numero: ")
chute = int(chute)

if (number_secret == chute):
  print("\n\tAcertou!\n＼(((￣(￣(￣▽￣)￣)￣)))／");
else:
  print("\n\tErrou...\n┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻");
  print("\nNumero Secreto: ", number_secret);

print('\n------\t Fim do Jogo\t ------');
