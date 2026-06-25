# b) f(x) = sin(x) no intervalo [0, π]

# Importação da biblioteca math, que fornece a função math.cos(x) e a constate pi utilizadas neste código
import math

# Definição da primitiva da função sin(x)
def F(x):    
    return  math.cos(x) * - 1 

# Limites inferior e superior
a = 0
b = math.pi

# Cálculo da integral definida
integral = F(b) - F(a) 

# Saída do resultado
print("O valor da integral é:", integral) 