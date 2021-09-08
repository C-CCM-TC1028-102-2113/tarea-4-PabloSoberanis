def main():
    n = int(input('Ingrese la cantidad a repetir los símbolos: '))

    for numero in range (n):
        if numero % 2 == 0:
            print('#')
        else:
            print('%')
if __name__ == '__main__':
    main()
