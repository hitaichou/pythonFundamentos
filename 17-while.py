#lista de filmes
movieList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

#1 - interando valores de uma lista de filmes usando while
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1  # Incrementa o índice para evitar loop infinito
    
#2 - quando a condição for atendida, interrompe o loop
index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        break  # Interrompe o loop se encontrar "Inception"
    print(movieList[index])
    index += 1  # Incrementa o índice

#3 - quando a condição for atendida, pula para a próxima iteração
index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        index += 1  # Pula para a próxima iteração se encontrar "Inception"
        continue
    print(movieList[index])
    index += 1  # Incrementa o índice    
    
#4 - avaliação do filme com while
movieName = input("Digite o nome do filme:\n ")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n "))    

total = 0
count = 0
while count < movieRating:
    note = float(input("Digite a nota para o filme:\n "))
    total += note  # Soma as notas
    count += 1  # Incrementa o contador

if movieRating > 0:
    average = total / movieRating  # Calcula a média
else:
    average = 0
print(f"A média de avaliações do filme {movieName} é: {average:.2f}")