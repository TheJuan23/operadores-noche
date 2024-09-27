#Expresion 42//6+7*3-39
resultado0 = 42//6+7*3-39
resultado1 = (42//6)+7*3-39
resultado2 = (42//6)+(7*3)-39
resultado3 = ((42//6)+(7*3))-39
resultado4 = (((42//6)+(7*3))-39)
print(f"sin prioridad {resultado0}, con prioridad 3 // {resultado1}, con prioridad 3 * {resultado2}, "
      f"con prioridad 4 + {resultado3} y con prioridad 4 - {resultado4}")
