# Imprima los n números primos contenidos en un intervalo (por ejemplo los números primos del 1 al 10)

inicio = int(input("Ingrese inicio del intervalo: "))
fin = int(input("Ingrese fin del intervalo: "))
limite = inicio 
print(f"Los números primos del {inicio} al {fin} son: ")

while fin > limite:
  limite = inicio
  contador_residuo_0 = 0
  for i in range(1, inicio + 1):
     if inicio % i == 0:
      contador_residuo_0 += 1
  if contador_residuo_0 == 2:
    print(inicio)
  
  inicio += 1