def fibonacci(posicao):
    if posicao == 1 or posicao == 2:
        return 1
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)

posicao = int(input("Digite a posição na sequência de Fibonacci: "))
resultado = fibonacci(posicao)

print(f"O valor na posição {posicao} da sequência de Fibonacci é: {resultado}")

