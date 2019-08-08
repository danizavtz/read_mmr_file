
class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.quantidade_repeticoes = 0

    def __str__(self):
        return 'Nome: {}, idade: {}, email: {}'.format(self.nome, self.idade, self.email)

    def incrementa_repeticoes(self):
        self.quantidade_repeticoes += 1

    def __eq__(self, outro):
        if isinstance(outro, Pessoa):
            return self.nome == outro.nome and self.idade == outro.idade and self.email == outro.email
        return False