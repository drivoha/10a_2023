import math
a = float(input())
b = float(input())
c = float(input())
D = b**2-4*a*c
x1 = (-b + math.sqrt(D))/(2*a)
x2 = (-b-math.sqrt(D))/(2*a) 
if a != 0 and D>0:
    print(x1, x2, ' - корни уравнения ')
else:
    print("ПЕРВОЕ ЧИСЛО ДОЛЖНО БЫТЬ ПОЛОЖИТЕЛЬНЫМ, ТАКЖЕ С ДИСКРИМИНАНТОМ")
    
    
