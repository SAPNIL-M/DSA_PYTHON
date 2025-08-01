def reverse_int (x):
    ans=0
    if x>0:
        sign=1
    else:
        sign=-1
    x=abs(x)
    min=-(2**31)
    max=(2**31)-1
    while x!=0:
        n=x%10
        x=x//10
        if ans>max or ans ==max//10 and n>max%10:
            return 0
        ans=(ans*10)+n
    if ans>max or ans<min:
        return 0
    else :
        return ans*sign
    
print(reverse_int(-1056389759))