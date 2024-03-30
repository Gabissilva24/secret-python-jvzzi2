# Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

primeiro: int
segundo: int
terceiro: int
maior: int
menor: int


primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
maior = primeiro
menor = primeiro

if segundo > maior:
  maior = segundo
if terceiro > maior:
  maior = terceiro

print('O maior número é : ', maior)



if primeiro>segundo and primeiro>terceiro:
  print('primeiro é maior que segundo e terceiro')
elif segundo>primeiro and segundo>terceiro:
  print('segundo é maior que primeiro e terceiro')
else:
  print('terceiro é maior que primeiro e segundo')

if segundo < menor:
  menor = segundo
if terceiro < menor:
  menor = terceiro

print('O menor número é : ', menor)


if primeiro<segundo and primeiro<terceiro:
  print('primeiro é menor que segundo e terceiro')
elif segundo<primeiro and segundo<terceiro:
  print('segundo é menor que primeiro e terceiro')
else:
  print('terceiro é menor que primeiro e segundo')