import math

number1 = int(input('Enter number 1'))
number2 = int(input('Enter number 2'))
print(number1,number2)
sum=number1+number2
print(sum)
difference=number1-number2
multiplication=number1*number2
division=number1/number2
print(difference,multiplication,division)
number3 = int(input('Enter number 3'))
sum=number1+number2+number3
difference=number1-number2-number3
multiplication=number1*number2*number3
division=(number1/number2/number3)
print(sum)
print(difference,multiplication,division)
import math
math.pow(9,3)
print(math.pow(9,3))
math.ceil(17.89)
print(math.ceil(-17.89))
p=16
q=25
edistanc= int(math.dist([p],[q]))
print(math.dist([p],[q]))
e=math.exp(4)
print(e)
print(math.fabs(-10))
print(math.fabs(10))
math.floor(-15.99)
print(math.floor(-15.99))
print(math.fsum([-7, -8, -9, 7, 8,9]))
print(math.fmod(15,2))
print(math.gcd(64,8))
a=7.34
b=7.55
rel_tol= 4
abs_tol= 0
print(math.isclose(a,b))
print(math.isfinite(2023))
print(math.isfinite(-423))