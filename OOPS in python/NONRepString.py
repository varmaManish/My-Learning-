def Nonrepstring(s):
    count={}
    for ch in s:
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
    result=[]
    for ch in s:
        if count[ch]==1:
             result.append(ch)
    if not result:
        return "no repeating string"
    return result
print(Nonrepstring("abbbbc"))