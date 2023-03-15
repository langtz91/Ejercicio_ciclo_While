# 2. De los n elementos de la serie de fibonacci, diga cuántos son pares, y cuántos impares.

limite = int(input("Ingrese hasta que elemento de fibonacci desea llegar: "))
x1 = 0
x2 = 0
x3 = 1

par = 0
impar = 0

while limite != x1:
 
 x1 = x2
 x2 = x3 
 x3 = x1 + x2
 if x1 % 2 == 0:
     par += 1
 else:
     impar += 1 

 print(x1)
 

print(f"hay {par} elementos pares de la serie de fibonacci")
print(f"hay {impar} elementos impares de la serie de fibonacci")
