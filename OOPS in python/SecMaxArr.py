def sec_max(arr):
    if len(arr)<2:
        return "invalid input"
    max_val=arr[0]
    second_val=None
    for i in range(1,len(arr)):
        if arr[i]>max_val:
            second_val=max_val
            max_val=arr[i]
        elif second_val is None or arr[i]>second_val:
            if arr[i]!=max_val:
                second_val=arr[i]
        if second_val is None :
            return "NO second max"
    return second_val
arr=[4,6,80,57,68]
print(sec_max(arr))
