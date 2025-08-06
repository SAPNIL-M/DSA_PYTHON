def rotate_arr(nums,k):
    n=len(nums)
    k=k%n
    l,r=0,n-1
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r=r-1
    l,r=0,k-1
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r=r-1
    l,r=k,n-1
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r=r-1
    return nums

print(rotate_arr([1,2,3,4,5,6,7,8],3))