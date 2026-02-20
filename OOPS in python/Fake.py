def sec_max(num):
    n=len(num)
    if n<2:
        return "invalid input"
    max_val=num[0]
    sec_val=None
    for i in range(1,n):
        if num[i]>max_val:
            sec_val=max_val
            max_val=num[i]
        elif sec_val is None or num[i]>sec_val:
            if num[i]!=max_val:
                num[i]=sec_val
            if sec_val is None:
                return "second is Not define"
    return sec_val
num=[1,5,3,7,2,7]
print(sec_max(num))


def is_Sorted(numm):
    n=len(numm)
    if n==1:
        return "Sorted"
    i=0
    while i<n-1:
       if numm[i]>numm[i+1]:
        return False
       i+=1
    return "is sorted"
numm=[1,5,8,10]
print(is_Sorted(numm))

def rev(s):
    rev=" "
    for i in s:
        rev=i+rev
    if rev==s:
        print("palindrome")
    else:
        print("it is not")
s="mam"
rev(s)

#Bubble sort
arr=[4,8,5,6,9,1,10,0]
n=len(arr)
'''for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            #swap the arr value
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)'''
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
S=arr[::-1]
print(S[1])

array=[1,0,5,0,6]
pos=0
for i in range(len(array)):
    if array[i]!=0:
        array[pos],array[i]=array[i],array[pos]
        pos+=1
print(*array)