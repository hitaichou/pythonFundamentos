# 1 - imprime um nome completo
def full_name(first_name, last_name):
    print(f"Nome completo: {first_name} {last_name}")
    
full_name("Fulano", "Ciclano")

# 2 - função para calcular dois numeros
def sum_numbers(num1, num2):
    return num1 + num2
print(f"A soma dos números é: {sum_numbers(10, 20)}")

# 3 - função com parametro padrão (default)
def address(country="Brasil"):
    print(f"Eu modo em : {country}")

address()
address("Estados Unidos")

#4 - função para avaliar um filme
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        nota = float(input(f"Digite a nota para o filme {movie_name}:\n"))
        total += nota
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    
    print(f"A média das avaliações para o filme: {movie_name} é: {average:.2f}")
    
rate_movie(2, "O Senhor dos Anéis")
#rate_movie(2, "Harry Potter")
        
