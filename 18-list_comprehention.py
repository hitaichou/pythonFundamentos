#1 - listando valores de 0 a 10 que sejam menores do que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

#lista de filmes
movieList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

#2 - filmes que possuem a letra 'e' no título
moviesWithE = [movie for movie in movieList if 'e' in movie.lower()]
print(moviesWithE)

#3 - filmes que eu assisti
moviesWatched = [movies for movies in movieList if movies != "Jurassic Park"]
print(moviesWatched)

#4 - encontrando o filme pelo nome
while True:
    searchName = input("Digite o nome do filme que deseja encontrar (ou sair para encerrar):\n ")
    if searchName.lower() == "sair":
        print("Encerrando a busca.")
        break
    foundMovies = [movie for movie in movieList if searchName.lower() in movie.lower()]    
    if foundMovies:
        print(f"Filmes encontrados: {searchName}")
        for foundMovie in foundMovies:
            print(foundMovies)
    else:
        print(f"Nenhum filme encontrado com esse nome {searchName}. Tente novamente.")
    