class aluno():
    def __init__(self, num, nome, email, n1, n2):
        self._num = num
        self._nome = nome
        self._email = email
        self._n1 = n1
        self._n2 = n2
    _lista_alunos = []

    def incluir(self):
        aluno._lista_alunos.append(f'------{self._nome}------')

a1 = aluno('a','b','c','1','2')
a2 = aluno('x','y','z','3','4')
a2.incluir()
a1.incluir()
print(aluno._lista_alunos)