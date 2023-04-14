print("Consider a Quadratic Equation in x")
a=int(input("Enter coefficient of x^2"))
b=int(input("Enter coefficient of x"))
c=int(input("Enter constant term"))
discriminant=b*b-4*a*c
if discriminant==0:
  print("Roots are real and equal")
if discriminant>0:
  print("Roots are real and unequal")
if discriminant<0:
  print("Roots are imaginary")
power=0.5
s=discriminant**power
root1=((-b)+s)/2*a
root2=((-b)-s)/2*a
print(root1)
print(root2)
     

Output

Consider a Quadratic Equation in x
Enter coefficient of x^21
Enter coefficient of x-7
Enter constant term10
Roots are real and unequal
5.0
2.0

