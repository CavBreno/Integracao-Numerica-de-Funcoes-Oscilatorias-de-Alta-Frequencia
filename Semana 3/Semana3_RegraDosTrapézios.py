import math

def f(x):                                   # função f(x)
    return math.sin(x)                       # expressão da função a ser integrada

def trapezio_composto(f, a, b, n):
    dx = (b - a) / n                        # largura de cada subintervalo
    soma = 0                                # acumulador da soma

    for i in range(n):                      # percorre os subintervalos
        x_i = a + i * dx                    # extremidade esquerda do subintervalo
        x_ip1 = a + (i + 1) * dx            # extremidade direita do subintervalo
        soma += f(x_i) + f(x_ip1)           # soma das avaliações da função
    return (dx / 2) * soma                  # fórmula do trapézio composto

a = 0                                         # limite inferior
b = math.pi                                    # limite superior
n = [10, 20, 100]                                         # número de partições

print(" N  | Valor Aproximado | Valor Exato | Erro Absoluto")
for particoes in n:
    resultado = trapezio_composto(f, a, b, particoes)   # cálculo da integral
    erro = abs(2 - resultado)
    print(f"{particoes:04d} {resultado:^18.6f} {2:^13.6f} {erro:^14.8f}")

