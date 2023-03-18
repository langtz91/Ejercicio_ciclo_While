 #Dado dos números, determine el MCD (Máximo Común Divisor) entre ellos.

def max_comun_div(numero1, numero2):
    while numero2 != 0:
        residuo = numero1 % numero2
        numero1 = numero2
        numero2 = residuo
    return numero1

numero1 = int(input("Ingrese su primer número: "))
numero2 = int(input("Ingrese su segundo número: "))

mcd = max_comun_div(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es {mcd}")
