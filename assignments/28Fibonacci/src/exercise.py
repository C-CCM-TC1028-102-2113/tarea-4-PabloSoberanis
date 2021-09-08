
def main():
    #escribe tu código abajo de esta línea
    x = int(input("Enter a number: "))
    
    n1 = 0
    n2 = 1

    if x >= 0:
        if x == 0:
            print(n1)
        elif x == 1:
            print(n2)
        elif x >= 2:
            for y in range(x-1):
                nu = n1 + n2 
                n1 = n2
                n2 = nu
            print(nu)
    else:
        print("Invalid input")
    pass

if __name__=='__main__':
    main()
