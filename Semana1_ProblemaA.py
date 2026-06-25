# a) f(x) = x² no intervalo [0, 1]

# Definição da primitiva da função x²
def F(x):    
    return x**3 / 3  

# Limites inferior e superior
a = 0
b = 1

# Cálculo da integral definida
integral = F(b) - F(a) 

# Saída do resultado
print("O valor da integral é:", integral) 