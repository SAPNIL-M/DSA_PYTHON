def move_zeros(nums):    
    n=len(nums)
    left=0
    for right in range(n):
        if nums[right]!=0:
            nums[right],nums[left]=nums[left],nums[right]
            left+=1
    return nums

print(move_zeros([0,1,0,3,12]))