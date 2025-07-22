from dataclasses import dataclass


@dataclass
class cliente:
    nome: str
    email: str
    idade: int
    
    def exibir(self):
        print(
            f'meu nome {self.nome} , idade {self.idade}'
        )

guilherme = cliente(nome='Guilherme', email='gui@gui.com', idade=28)






# class cliente:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email

#     def exibir(self):
#         print(self.nome, self.idade)

# guilherme = cliente("Guilherme", "email@gmail.com")

# print(guilherme.email)