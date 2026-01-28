def fatorial(n):
    if n<0:
        return False
    res=1
    for i in range(2,n+1):
        res*=i
    return res
print(fatorial(5))


### Recursive method
def fact(num):
   if num<0:
       return False
   if num==0 or num==1:
     return 1
   return num*fact(num-1)
print(fact(5))
   