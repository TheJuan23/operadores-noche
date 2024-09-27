m = int( input("ingrese numero1 "))
n = int( input("ingrese numero2 "))
if m < n:
    numero1 = m
    numero2 = n
    menor = m
    mayor = n
else:
    numero1 = n
    numero2 = m
    menor = n
    mayor = m


if numero1 == numero2:
    print(f"los numeros {n} y {m} son iguales")

else:
    resta = mayor-menor
    iguales = (resta+menor)
    print(f"los numeros {m} y {n} serian iguales solo si se hace la suma de {menor} y {resta}")


q = 5
print(q > 4 and q < 9)
print(q > 4 or q < 10)
print(not (q > 2 and q < 7))