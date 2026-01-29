#Iterative method
def fibonacci(n):
    if n<0:
        return "invalid input"
    if n in (0,1):
        return n
    a,b= 0,1
    for _ in range(2,n+1):
        a,b = b,a+b
    return b
print(fibonacci(5))

#Recursive method

def fib(num):
    if num<0:
        return "invalid input"
    if num in (0,1):
        return num
    return fib(num-1)+fib(num-2)
print(fib(7))