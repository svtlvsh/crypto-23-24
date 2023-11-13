most_popular_bigrams = ["ст", "но", "то", "на", "ен"]
alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"

def GCD(a,b):
    if b == 0:
        return a, 1, 0
    d, x, y = GCD(b, a % b)
    return d, y, x - (a // b) * y

result = GCD(144, 120)
print("НСД: ", result[0])
print("Коефіцієнти x, y: ", result[1], result[2])

def mod_inv(a, m):
    gcd, x, y = GCD(a, m)
    if gcd != 1:
        raise ValueError(f"Не існує оберненого")
    else:
        return x % m

def solve_linear_congruence(a, b, m):
    gcd, x, y = GCD(a, m)
    if b % gcd == 0:
        x0 = (x * (b // gcd)) % m
        solutions = [(x0 + k * (m // gcd)) % m for k in range(gcd)]
        return solutions
    else:
        return []
