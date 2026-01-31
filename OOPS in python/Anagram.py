def isanagram(s1,s2):
    if len(s1)!=len(s2):
        print("is not a anagram")
    freq={}
    for ch in s1:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in s2:
        if ch not in freq or freq[ch]==0:
            return False
        freq[ch]-=1
        break            
    return True
print(isanagram("silent","listen"))
print(isanagram("hello","world"))