# c) f(x) = e^x no intervalo [0, 1]

# Importação da biblioteca math, que fornece a constante e utilizada neste código
import math

# Definição da primitiva da função e^x
def F(x):  
    return math.exp(x) 

# Limites inferior e superior
a = 0
b = 1

# Cálculo da integral definida
integral = F(b) - F(a) 

# Saída do resultado
print("O valor da integral é:", integral) 