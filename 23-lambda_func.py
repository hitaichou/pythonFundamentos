#para que serve a função lambda?
# A função lambda é uma forma concisa de definir funções anônimas em Python.
# Elas são úteis para criar funções simples e rápidas, especialmente quando você não precisa reutilizar a função em outro lugar.
# As funções lambda são frequentemente usadas em operações de mapeamento, filtragem e redução, como em funções como `map()`, `filter()` e `reduce()`.
# Elas permitem que você escreva código mais limpo e legível, evitando a necessidade de definir funções nomeadas para tarefas simples.
# Além disso, as funções lambda são úteis em contextos onde você precisa passar uma função como argumento, como em callbacks ou funções de ordem superior.

#função potencia de um numero
power = lambda num: num ** 2


#função que verifica se o numero é par
is_even = lambda num: num % 2 == 0 #se resultado é igual a 0, é par

#função que divide um numero por outro
divide = lambda x, y: x / y 

#função que divide uma string
reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(27))
print(is_even(30))
print(divide(10, 2))
print(divide(6, 2))
print(reverse_string("Python"))
print(reverse_string("JavaScript"))

#funcionalidades relacionadas aos filmes:
movies_list = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic": [8.7, 9.0, 8.5],
    "The Godfather": [9.5, 9.8, 8.0],
    "Inception": [8.0, 7.0, 8.5],
    "Jurassic Park": [8.5, 8.7, 8.6],
    "The Matrix": [8.9, 9.1, 9.0]
}
# Função lambda para calcular a média de avaliações de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f"Média do filme The Matrix: {average_rating('The Matrix')}")

#função que verifica se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list

print(f"Está o filme Titanic na lista? {check_movie('Inception')}")

#função para recomendar um filme baseado na média de avaliações
#recommend_movie = lambda movie_name: f"Recomendamos assistir {movie_name}!" if average_rating(movie_name) > 8.5 else f"Recomendamos não assistir {movie_name}."
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name)}"

print(f"{recommend_movie('The Godfather')}")




    
