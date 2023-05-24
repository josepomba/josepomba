def area(lado, comprimento=None):
    if comprimento == None:
        print(lado * lado)

    else:
        print(lado * comprimento)


def perimetro(lado, comprimento=None):
    if comprimento == None:
        print(lado*4)
    else:
        print(lado*2+comprimento*2)

__version__ = '0.1'
