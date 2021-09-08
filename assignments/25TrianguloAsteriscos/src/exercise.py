
def main():
    #Escribe tu código debajo de esta línea
    a = int(input("altura?"))
    b = a

    for x in range(a):
    b = b - 1
    c = "*" * (x+1) 
    print(" " * b + c)
    pass


if __name__=='__main__':
    main()
