def valid_anagram(s,t):
    count={}
    for item in s:
        if item in count:
            count[item]+=1
        else:
            count[item]=1
    for item in t:
        if item in count:
            count[item]-=1
    for val in count.values():
        if val!=0:
            return False
    return True

print(valid_anagram("anagram","nagaram"))

