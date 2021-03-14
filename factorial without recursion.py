def recur_factorial(n):
if  n == 1:
return n
return n*recur_factorial(n-1)
num = 7
# we will check if the number is negative
if num<0:
print(“Factorial does not exist for negative numbers”)
elif num == 0:
print(“The factorial of 0 is 1”)
else:
print(“The factorial of”, num, “ïs” , recur_factorial(num))
