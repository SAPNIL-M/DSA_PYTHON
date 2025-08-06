def max_prod_subarray(nums):
    pre=suf=1
    ans=float('-inf')
    n=len(nums)
    for i in range(n):
        pre*=nums[i]
        suf*=nums[n-1-i]
        ans=max(ans,pre,suf)
        if pre==0 : pre=1
        if suf==0 : suf=1
    return ans

print(max_prod_subarray([-1, -2, -3, -4]))