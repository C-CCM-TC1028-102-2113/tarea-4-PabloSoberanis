

def main():
    #Escribe tu código debajo de esta línea
    num = int(input("Escribe un numero : "))
    n = 1

    while n **2 <= num:
        n += 1
    print(n)
    pass

if __name__=='__main__':
    main()
