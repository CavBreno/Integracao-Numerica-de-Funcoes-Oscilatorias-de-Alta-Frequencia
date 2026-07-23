import math

# Definição da função a ser integrada
def f(x):                         # função f(x)
    return math.exp(x)            # expressão da função f(x)

# Implementação da Soma de Riemann
def riemann (f, a, b, n):
    dx = (b - a) / n              # largura de cada subintervalo
    
    soma = 0                      # inicialização do acumulador
    
    for i in range(n):            # percorre os subintervalos
    
        x = a + i * dx            # ponto esquerdo do subintervalo

        soma += f(x)              # acumula valor da função

    return soma * dx              # aproximação final da integral

# Definição do intervalo de integração
a = 0                             # limite inferior
b = 1                             # limite superior

# Número de subintervalos
n = 10                        # quantidade inicial de partições

print(" N  | Valor Aproximado | Valor Exato | Erro Absoluto")
for i in range(1, 4):
    
    # Cálculo da aproximação da integral
    resultado = riemann (f, a, b, n)

    # Exibição do resultado obtido
    print(f"{n:04d} {resultado:^18.6f} {1.71828:^13.6f} {1.71828 - resultado:^14.8f}")

    n *= 10

