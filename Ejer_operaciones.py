#Realice un programa que muestre un menú con las siguientes opciones:
#1) Sumar
#2) Restar
#3) Multiplicar
#4) Dividir
#5) Salir
#El usuario debe seleccionar una opción, y a continuación, el programa
#debe solicitar el ingreso de dos números enteros y debe realizar la
#operación correspondiente a la opción seleccionada. La ejecución debe
#realizarse una y otra vez, hasta que el usuario seleccione la opción #5.

print("1) Sumar") 
print("2) Restar") 
print("3) Multiplicar") 
print("4) Dividir")
print("5) Salir")

opcion= int(input("Seleccione la opción deseada ingresando el número correspondiente: ")) 
     
while opcion !=  5:
  while opcion > 5:
     print("Elegiste una opción incorrecta")
     opcion= int(input("Seleccione la opción deseada ingresando el número correspondiente: "))
  if opcion == 5:
     break  
  numero1 =int(input("Ingrese el primer número: "))
  numero2 =int(input("Ingrese el segundo número: "))
  if opcion == 1:
     operacion = "sumar" 
     total = numero1 + numero2
  elif opcion == 2:
     operacion = "restar" 
     total = numero1 - numero2
  elif opcion == 3:
     operacion = "multiplicar"
     total = numero1 * numero2
  elif opcion == 4:
     operacion = "dividir"
     total = numero1 / numero2
  elif opcion > 5:
     print("Elegiste una opción incorrecta")
  
  print(f"El resultado de {operacion} es: {total}")

  opcion= int(input("Seleccione la opción deseada ingresando el número correspondiente: "))

  


 