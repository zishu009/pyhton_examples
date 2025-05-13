# -------------------------------- Example 1
'''
import time 
def countdown(num):
  print('Count Down starting....')

  while num > 0:
    yield num
    num = num - 1

values = countdown(5)
for x in values:
  print(x)
  time.sleep(1)
'''

# ------------------- Example 
'''
def firstn(num):
  n = 1
  while n <= num:
    yield n 
    n = n + 1

for x in firstn(10):
  print(x)
'''
# -------------------------- Example 3
# --------------- Generate fibonacci number
'''
def fib():
  a , b = 0 , 1
  while True:
    yield a 
    a , b = b , a + b

for n in fib():
  if n > 100:
    break
  print(n)
'''


# --------------------- Factorial
# Factorial using for loop
'''
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
'''


# ----------------- by using recursion
# Factorial using recursion

def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")













