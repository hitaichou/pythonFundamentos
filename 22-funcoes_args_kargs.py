"""
*args = utilizamos ele quando não temos certeza de quantos argumentos serão passados para a função.
- Os argumentos são passados como uma tupla.

**kwargs = além dos valores, podemos passar também as respectivas chaves para cada argumento.
# Isso é útil quando queremos passar um número variável de argumentos nomeados para a função.
- Os argumentos são passados como um dicionário.
 
"""

# 1 - soma de numeros
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"A soma dos números é: {sum_total}")

sum(7,9,10,11)


# 3 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print("Lista de cursos:")
presentation(name="Python", category="Backend", Level="Iniciante")
presentation(name="Visão Computacional com Python", category="AI", Level="Avançado")
presentation(name="Dashboard com Dash", category="Data Science", Level="Intermediario")

