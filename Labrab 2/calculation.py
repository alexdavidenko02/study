import math
def calculate_z():
    alpha = float(input("Введіть значення alpha: "))
    z = (math.sqrt(2) / 2) * math.sin(alpha / 2)
    return z
def amoeba_count(n):
    return 2 ** (n // 3)
