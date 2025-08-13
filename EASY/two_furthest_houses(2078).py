def two_houses(colors):
    ans=0
    n=len(colors)
    for i in range(n):
        if colors[i]!=colors[0]:
            ans=max(ans,i)
        if colors[i]!=colors[-1]:
            ans=max(ans,n-1-i)
    return ans

print(two_houses([1,8,3,8,3]))