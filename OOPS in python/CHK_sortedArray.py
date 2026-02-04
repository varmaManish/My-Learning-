def is_sorted(arr):
    n=len(arr)
    if n<=1:
        return True
    i=0
    while i < n-1:
       if arr[i]>arr[i+1]:
           return False
       i+=1
    return "sorted"
arr=[1,2,3,4,5,6]
print(is_sorted(arr))
