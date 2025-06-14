filmsTuple = ("Inception", "The Shawshank Redemption", 
            "The Dark Knight", "Pulp Fiction",
            "Interstellar")
#print(type(filmsTuple))  # Output: <class 'tuple'>            

#1 - buscar os dois primeiros filmes da tupla
print(filmsTuple[:2])  # Output: ('Inception', 'The Shawshank Redemption')

#2 - buscar o últimos filme da tupla
print(filmsTuple[-1])  # Output: Interstellar

#3 - buscar filmes até uma determinada posição
print(filmsTuple[:3])  # Output: ('Inception', 'The Shawshank Redemption', 'The Dark Knight')

#4 - buscar filmes de uma posição em diante
print(filmsTuple[2:])  # Output: ('The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction')

#5 - recuperar um item da tupla pelo nome
print(filmsTuple.index("Pulp Fiction"))  # Output: 3



