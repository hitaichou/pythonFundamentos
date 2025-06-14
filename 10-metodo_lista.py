filmList = ["Inception", "The Shawshank Redemption", 
            "The Dark Knight", "Pulp Fiction",
            "Interstellar"]

#1 - tamanho da lista
print(len(filmList))  # Output: 5
#2 - recuperar um item da lista pelo nome
print(filmList.index("Interstellar"))  # Output: 4
#3 - adicionar um item no final da lista
filmList.append("The Lord of the Rings")
print(filmList)  # Output: ['Inception', 'The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction', 'Interstellar', 'The Lord of the Rings']
#4 - ordernar a lista
filmList.sort()
print(filmList)  # Output: ['Inception', 'Interstellar', 'Pulp Fiction', 'The Dark Knight', 'The Lord of the Rings', 'The Shawshank Redemption']
#5 - copiar os itens de uma lista
filmCopy = filmList.copy()
filmCopy.remove("Pulp Fiction")
print(filmCopy)  # Output: ['Inception', 'Interstellar', 'The Dark Knight', 'The Lord of the Rings', 'The Shawshank Redemption']

#6 - remove todos os itens da lista
filmList.clear()
print(filmList)  # Output: []