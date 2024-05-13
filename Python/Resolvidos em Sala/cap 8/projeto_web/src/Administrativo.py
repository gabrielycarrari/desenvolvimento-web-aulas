from Funcionario import Funcionario


class Administrativo(Funcionario):
    def __init__(self, nome, idade, setor):
        super().__init__(nome, idade)
        self.setor = setor

    def calcular_salario(self) -> float:
        return 4000