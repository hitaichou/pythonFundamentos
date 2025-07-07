"""
Fatorial de um numero:
1 -> 1 * 1 = 1
2 -> 2 * 1 = 2  (2 * fatorial(1))
3 -> 3 * 2 * 1 = 6 (3 * fatorial(2))
"""

# 1 - fatorial de um numero
def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))
    
number = int(input("Digite um número para calcular o fatorial:\n"))
print(f"O fatorial de {number} é: {fatorial(number)}")

# 2 - soma total de um numero
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))

num = int(input("Digite um número para calcular a soma:\n"))
print(f"A soma total de {num} é: {total_sum(num)}")
        