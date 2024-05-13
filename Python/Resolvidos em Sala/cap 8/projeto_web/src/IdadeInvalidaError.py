class IdadeInvalidaError(Exception):
    def __init__(self, idade):
        super().__init__(f"A idade {idade} não é válida. Deve estar entre 0 e 120.")