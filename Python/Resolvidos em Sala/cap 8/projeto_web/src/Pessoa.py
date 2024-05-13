from IdadeInvalidaError import IdadeInvalidaError


class Pessoa:
    contador = 0
    def __init__(self, nome, idade):
        self.nome = nome.upper()
        self.idade = idade
        Pessoa.contador += 1

    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, valor: int):
        if 0 <= valor <= 120:
            self.__idade = valor
        else:
            raise IdadeInvalidaError(valor)
    
    def falar(self, mensagem):
        print(f"{self.nome} falou '{mensagem}'.")

    @classmethod
    def mostrar_qtde_objetos(cls):
        print(f"Foram instanciados {cls.contador} objetos da classe Pessoa")
    
        