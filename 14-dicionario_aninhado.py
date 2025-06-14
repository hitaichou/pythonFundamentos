#Este exemplo mostra como criar um dicionário aninhado para armazenar informações sobre filmes.

import pprint #este módulo é usado para imprimir dicionários de forma mais legível

filmIDict = {
    "inception": {
        "title": "Inception",
        "year": 2010,
        "imdbRating": 8.8,
        "genres": ["Action", "Action", "Sci-Fi"]
    },
    "interstellar": {
        "title": "Interstellar",
        "year": 2014,
        "imdbRating": 8.6,
        "genres": ["Drama", "Sci-Fi"]
    },
    "the dark knight": {
        "title": "The Dark Knight",
        "year": 2008,
        "imdbRating": 9.0,
        "genres": ["Action", "Crime", "Drama"]
    }
}

print(type(filmIDict))  # Output: <class 'dict'>

#exemplo em como imprimir o dicionário de forma mais legível
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmIDict)

#1 - buscar uma informação dentro de um dicionario aninhado
print(filmIDict["interstellar"]["genres"])  # Output: ["Drama", "Sci-Fi"]

#2 - adicionar um novo item
filmIDict["inception"]["director"] = "Christopher Nolan"
print(filmIDict["inception"])  # Output: {'title': 'Inception', 'year': 2010, 'imdbRating': 8.8, 'genres': ['Action', 'Action', 'Sci-Fi'], 'director': 'Christopher Nolan'}

#3 - excluir um dicionário aninhado
del filmIDict["the dark knight"]
pp.pprint(filmIDict)  # Output: {'inception': {'title': 'Inception', 'year': 2010, 'imdbRating': 8.8, 'genres': ['Action', 'Action', 'Sci-Fi'], 'director': 'Christopher Nolan'}, 'interstellar': {'title': 'Interstellar', 'year': 2014, 'imdbRating': 8.6, 'genres': ['Drama', 'Sci-Fi']}}


