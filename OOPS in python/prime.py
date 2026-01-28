n=29
flag=0
for i in range (2,n):
   if  n%i==0:
    flag=1
    break
if flag==1:
    print("this is not a prime")
else:
    print("this is a prime")