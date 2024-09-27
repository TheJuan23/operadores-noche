#Aritmeticos
from OperadoresAritmeticos import numero1, numero2

numero3 = int( input("Ingrese el numero1"))
numero4 = int( input("Ingrese el numero"))
suma = numero3 + numero4
resta = numero3 - numero4
division = numero3 / numero4
multiplicacion = numero3 * numero4
modulo = numero3 % numero4
divisionEntera = numero3 //numero4
print(f"la suma de {numero3} + {numero4} es: {suma} ")
print(f"la resta de {numero3} - {numero4} es: {resta} ")
print(f"la divicion de {numero3} / {numero4} es: {division} ")
print(f"la multiplicacion de {numero3} * {numero4} es: {multiplicacion} ")
print(f"el modulo de {numero3} % {numero4} es: {modulo} ")
print(f"la division entera de {numero3} // {numero4} es: {divisionEntera} ")
sumaTotal = numero1 + numero2 + numero3 + numero4
print(f"la suma de {numero1}, {numero2}, {numero3} y {numero4} es : {sumaTotal}")