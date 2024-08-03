def contador(limite, numero=0):
    if numero <= limite:
        print(numero)
        contador(limite, numero + 1)

limite = int(input("Digite um número: "))
contador(limite)
