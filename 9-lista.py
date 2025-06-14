filmMatrix = ["Matrix", 1999, 8.7, True]
#print(type(filmMatrix))
print(filmMatrix)  # Output: Toda lista

filmList = ["Inception", "The Shawshank Redemption", 
            "The Dark Knight", "Pulp Fiction",
            "Interstellar"]

#1 - buscar os dois primeiros filmes da lista
print(filmList[:2])  # Output: ['Inception', 'The Shawshank Redemption']
#2 - buscar o últimos filme da lista
print(filmList[-1])  # Output: Interstellar
#3 - buscar filmes até uma determinada posição
print(filmList[:3])  # Output: ['Inception', 'The Shawshank Redemption', 'The Dark Knight']
#4 - buscar filmes de uma posição em diante
print(filmList[1:4])  # Output: ['The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction']