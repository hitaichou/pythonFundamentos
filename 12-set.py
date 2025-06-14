filmsSet = {"Inception", "The Shawshank Redemption", 
            "The Dark Knight", "Pulp Fiction",
            "Interstellar"}

print(type(filmsSet))  # Output: <class 'set'>

#1 - buscar o tamanho do set
print(len(filmsSet))  # Output: 5

#2 - True e 1 são considerados o mesmo valor
exampleSet = {"Inception", True, 1, 8.7}
print(exampleSet)  # Output: {'Inception', True, 1, 8.7}

#3 - adicionar item de outro set
filmsSet.update(exampleSet)
print(filmsSet) 

#4 - remover um item do set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)