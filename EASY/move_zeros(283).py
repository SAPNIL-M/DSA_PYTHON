def move_zeros(nums):    
    count =0
    n=len(nums)
    for i in range(n-1,-1,-1):
        if nums[i]==0:
            count=count+1
            nums.pop(i)
            
    for i in range(count):
        nums.append(0)

    print(nums)

move_zeros([0,1,0,3,12])