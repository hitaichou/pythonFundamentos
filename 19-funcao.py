# 1 - função para imprimir uma mensagem
#def welcome():
#    print("Bem vindo ao sistema de filmes!")

#welcome()

#for i in range(10):
#    welcome()

# 2 - função para calcular a média de notas
def calculate_average():
    num_rating = int(input("Digite quantas avaliaçãoes deseja fazer pro filme:\n"))
    total = 0
    for i in range(num_rating):
        note = float(input(f"Digite a nota para o filme:\n"))
        total += note
    
    if num_rating > 0:
        average = total / num_rating
    else:
        average = 0
    return average



#calculate_average()

print(f"A média das avaliações é: {calculate_average():.2f}")


# 3 - função para cadastrar um filme
def create_movie():
    name = input("Digite o nome do filme:\n")
    yearLaunch = input("Digite o ano de lançamento do filme:\n")
    noteMovie = float(input("Digite a nota do filme:\n"))
    moviePrice = float(input("Digite o preço do filme:\n"))
    rating = float(input("Digite a avaliação do filme:\n"))
    print(f"{name} ({yearLaunch}) - R$ {moviePrice:.2f}")
    
create_movie()
create_movie()
    