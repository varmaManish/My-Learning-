def Max_num(num):
    if not num:
        return "it s empty"
    max=num[0]
    for i in range(1,len(num)):
        if num[i]>max:
           max=num[i]
    return max
num=[4,8,3,9,18]
print(Max_num(num))
