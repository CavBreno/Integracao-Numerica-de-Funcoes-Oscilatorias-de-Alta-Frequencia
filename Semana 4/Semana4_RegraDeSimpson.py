import math

def f(x):                                                   # função f(x)
    return pow(x, 3)                                        # expressão da função a ser integrada

def simpson_composto(f, a, b, n):                           # regra de Simpson composta

    if n % 2 != 0:                                          # verifica se n é par
        print("n deve ser par para a regra de Simpson")     # mensagem de erro
        return None                                         # interrompe execução
    
    dx = (b - a) / n                                        # largura de cada subintervalo
    soma = f(a) + f(b)                                      # inicia soma com extremos

    for i in range(1, n):                                   # percorre pontos internos
        x = a + i * dx                                      # ponto da partição

        if i % 2 == 0:                                      # se índice é par
            soma += 2 * f(x)                                # peso 2 (pontos pares)
        else:                                               # se índice é ímpar
            soma += 4 * f(x)                                # peso 4 (pontos ímpares)

    return (dx / 3) * soma                                  # fórmula final de Simpson

a = 0                                                       # limite inferior
b = 1                                                       # limite superior
n = [10, 20, 100]                                           # número de subintervalos (par)

print(" N  | Valor Aproximado | Valor Exato | Erro Absoluto")
for particoes in n:
    resultado = simpson_composto(f, a, b, particoes)   # cálculo da integral
    erro = abs(0.25 - resultado)
    print(f"{particoes:04d} {resultado:^18.6f} {0.25:^13.6f} {erro:^14.8f}")
