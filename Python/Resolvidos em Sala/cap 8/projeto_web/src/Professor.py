from Funcionario import Funcionario


class Professor(Funcionario):
    def __init__(self, nome, idade, siape):
        super().__init__(nome, idade)
        self.siape = siape

    def calcular_salario(self) -> float:
        return 5000
        