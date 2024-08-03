def contador(numero):
    if numero < 0:
        return
    print(numero)
    contador(numero-1)
    
numero = int(input("Digite um número: "))
contador(numero)
