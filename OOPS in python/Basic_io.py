def main():
    n=int(input())
    arr=[]
    for i in range(n):
        temp=int(input())
        arr.append(temp)
    if sum(arr)<100:
        print("yes")
    else:
        print("no")
main()
