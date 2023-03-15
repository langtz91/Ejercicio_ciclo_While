 #Dado dos números, determine el MCD (Máximo Común Divisor) entre ellos.

numero1 = int(input("Ingrese su primer número: "))
numero2 = int(input("Ingrese su segundo número: "))
numero1_1 = numero1
numero2_2 = numero2

while numero2 != 0:
    residuo = numero1 % numero2
    numero1 = numero2
    numero2 = residuo

print(f"El MCD de {numero1_1} y {numero2_2} es {numero1}")
