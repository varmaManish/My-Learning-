# loop based iteration
def string(value):
    rev=""
    for i in value:
        rev=i+rev
    return rev
print(string("hello jbdfb"))


# two Pointer approch

def rev(s):
    char=list(s) # mutable can be access after iteration
    left ,right=0,len(char)-1
    while left<right:
        char[left],char[right]=char[right],char[left]
        left+=1
        right-=1
    return "".join(char)
print(rev("hello"))