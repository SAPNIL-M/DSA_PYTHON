def sort_colors(nums):
    left=0
    n=len(nums)
    right=n-1
    i=0
    while i<=right:
        if nums[i]==0:
            swap(nums,i,left)
            left+=1
        elif nums[i]==2:
            swap(nums,i,right)
            right-=1
            i-=1
        i+=1
    return nums
def swap(nums,e1,e2):
    nums[e1],nums[e2]=nums[e2],nums[e1]
    return nums

print(sort_colors([2,0,2,1,1,0]))

