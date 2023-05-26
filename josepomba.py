def area(lado, comprimento=None):
    """ Devolve a area de um quadrado (se apenas for dado um argumento) ou de um retângulo (se forem dados dois argumentos) """
    if comprimento == None:
        print(lado * lado)

    else:
        print(lado * comprimento)


def perimetro(lado, comprimento=None):
    """ Devolve o perimetro de um quadrado (se apenas for dado um argumento) ou de um retângulo (se forem dados dois argumentos) """
    if comprimento == None:
        print(lado*4)
    else:
        print(lado*2+comprimento*2)

__version__ = '0.1'
