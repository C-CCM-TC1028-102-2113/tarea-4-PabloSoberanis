def main():
    cal = 0
    sum = 0
    i = 0
    prom = 0

    while True:
        if cal >= 0:
            cal = float(input('Introduce cal: '))
            sum = sum + cal 
            i= i + 1
        elif cal < 0:
            sum = sum - cal
            i = i- 1
            prom = sum / i
            print('El promedio es: ', str(prom))
            break
if __name__ == '__main__':
    main()
