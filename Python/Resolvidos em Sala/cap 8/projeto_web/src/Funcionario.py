from abc import abstractmethod
from Pessoa import Pessoa


class Funcionario(Pessoa):

    @abstractmethod
    def calcular_salario(self) -> float:
        pass