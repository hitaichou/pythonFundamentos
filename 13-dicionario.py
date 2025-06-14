# Dicionário é um tipo de coleção de dados com propriedades chave-valor
filmInception = {
    "title": "Inception",
    "year": 2010,
    "imdbRating": 8.8,
    "genres": ["Action", "Action", "Sci-Fi"],
}
print(filmInception)
print(len(filmInception))  # Output: 4
print(type(filmInception))  # Output: <class 'dict'>

#1 - recuperar um elemento do dicionário
print(filmInception["genres"])  # Output: ["Action", "Action", "Sci-Fi"]
print(filmInception.get("imdbRating"))  # Output: 8.8

#2 - buscar apenas as chaves do dicionário
print(filmInception.keys())  # Output: dict_keys(['title', 'year', 'imdbRating', 'genres'])

#3 - buscar apenas os valores do dicionário
print(filmInception.values())  # Output: dict_values(['Inception', 2010, 8.8, ['Action', 'Action', 'Sci-Fi']])

#4 - buscar itens do dicionario com chave e valor
print(filmInception.items())  # Output: dict_items([('title', 'Inception'), ('year', 2010), ('imdbRating', 8.8), ('genres', ['Action', 'Action', 'Sci-Fi'])])

#5 - adicionar itens no dicionário
filmInception["director"] = "Christopher Nolan"
print(filmInception)  # Output: {'title': 'Inception', 'year': 2010, 'imdbRating': 8.8, 'genres': ['Action', 'Action', 'Sci-Fi'], 'director': 'Christopher Nolan'}

#6 - atualizar itens no dicionário
filmInception.update({"imdbRating": 8.7})
print(filmInception)  # Output: {'title': 'Inception', 'year': 2010, 'imdbRating': 8.7, 'genres': ['Action', 'Action', 'Sci-Fi'], 'director': 'Christopher Nolan'}

#7 - remover itens do dicionário
filmInception.pop("director")
print(filmInception)  # Output: {'title': 'Inception', 'year': 2010, 'imdbRating': 8.7, 'genres': ['Action', 'Action', 'Sci-Fi']}