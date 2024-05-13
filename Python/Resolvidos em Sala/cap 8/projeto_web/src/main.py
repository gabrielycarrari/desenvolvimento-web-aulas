from typing import List
from Administrativo import Administrativo
from ESetor import ESetor
from Funcionario import Funcionario
from IdadeInvalidaError import IdadeInvalidaError
from Professor import Professor
from Pessoa import Pessoa

try:
    funcionarios: List[Funcionario] = []
    funcionarios.append(Professor("Fulano", 30, "123456"))
    funcionarios.append(Administrativo("Sicrano", 21, ESetor.COMPRAS))
    funcionarios.append(Professor("Beltrano", 23, "654321"))
    funcionarios.append(Administrativo("Fortrano", 21, ESetor.ENSINO))
    funcionarios.append(Professor("Pentano", 23, "456545"))
    funcionarios.append(Administrativo("Hexano", 21, ESetor.RECURSOS_HUMANOS))
    funcionarios.append(Professor("Hepnato", 132, "788987"))
except IdadeInvalidaError as ex:
    print(ex)
except Exception as ex:
    print(f"Erro {ex}")
finally:
    Pessoa.mostrar_qtde_objetos()

for f in funcionarios:
    print(f"{f.nome} recebe {f.calcular_salario()} por mês.")
    if type(f) is Administrativo:
        print(f"Setor: {f.setor.name}")

