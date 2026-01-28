n=151
temp=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("this is not palindrome")

m="mom"
rev=""
for  i in m:
    rev=i+rev
if rev==m:
    print("palindrome")
else:
    print("not")