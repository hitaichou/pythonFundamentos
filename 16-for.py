#lista de filmes
movieList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]


#1 - iterando valores de uma lista
for movie in movieList:
    print(movie)
    
#2 - quando a condição for atendida, interrompe o loop    
for movie in movieList:
    if movie == "Inception":
        break  # Interrompe o loop se encontrar "Inception"
    print(movie)
    
#3 - quando a condição for atendida, pula para a próxima iteração
for movie in movieList:
    if movie == "Inception":
        continue  # Pula para a próxima iteração se encontrar "Inception"
    print(movie)
    
#4 - avaliação do filme:
movieName = input("Digite o nome do filme:\n ")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n "))

total = 0

for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n "))
    total += note  # Soma as notas
    
if movieRating > 0:
    average = total / movieRating  # Calcula a média
else:
    average = 0
print(f"A média de avaliações para o filme {movieName} é: {average:.2f}")