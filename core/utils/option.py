from types import FunctionType, MethodType


class Option:
    def __init__(self, titulo:str, acao:FunctionType | MethodType):
        self.titulo = titulo
        self.acao = acao
