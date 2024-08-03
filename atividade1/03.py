def soma(n):
    if n < 1:
        return 0
    elif n % 2 == 1:
        return n + soma(n - 2)
    else:
        return soma(n - 1)

n = int(input("Digite um número: "))

print("A soma de todos os números naturais ímpares menores ou iguais a", n, "é:", soma(n))
