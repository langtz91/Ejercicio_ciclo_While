# Imprima los n números primos contenidos en un intervalo (por ejemplo los números primos del 1 al 10)

def es_primo(a):
  contador_residuo_0 = 0
  for i in range (1, a+1):
    if a % i == 0:
     contador_residuo_0 += 1
  return contador_residuo_0 == 2

inicio = int(input("Ingrese inicio del intervalo: "))
fin = int(input("Ingrese fin del intervalo: ")) 
print(f"Los números primos del {inicio} al {fin} son: ")

while fin > inicio:
  if es_primo(inicio):
    print(inicio)
  
  inicio += 1