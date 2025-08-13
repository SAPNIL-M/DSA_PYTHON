def rearrange_array_elements(nums):
    n=len(nums)
    i,j=0,1
    ans=[0]*n
    for val in nums:
        if val>0:
            ans[i]=val
            i+=2
        else:
            ans[j]=val
            j+=2
    return ans

print(rearrange_array_elements([3,1,2,-2,-1,-6]))