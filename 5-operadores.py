num1 = int(input("Digite o primeiro número:\n "))
num2 = int(input("Digite o segundo número:\n "))

#Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
Mod = num1 % num2
exp = num1 ** num2

print("Soma: ", sum)
print("Subtração: ", sub)
print("Divisão: ", div)
print("Multiplicação: ", mult)
print("Resto Divisão: ", Mod)
print("Exponenciação: ", exp)

print(f"Potência do número {num1} por {num2} é igual a {exp}")
print(f"Resto da divisão de {num1} por {num2} é igual a {Mod}")

#Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f"Os números {num1} e {num2} são iguais?")
print(f"O número {num1} é maior ou igual a {num2}? {biggerEqual}")

#Atribuição
num1 += 1 # num1 = num1 + 1
print(num1)
num1 -= 1 # num1 = num1 - 1
print(num1)
num1 *= 1 # num1 = num1 * 1
print(num1)
num1 /= 1 # num1 = num1 / 1
print(num1)

