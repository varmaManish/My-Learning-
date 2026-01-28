n=153
temp=n
count=0

while temp>0:
    count+=1
    temp//=10

temp=n
arm=0
while temp>0:
    d=temp%10
    arm+=d**count
    temp//=10
if arm==n:
    print("armstrong")
else:
    print("it's not a armstrong")