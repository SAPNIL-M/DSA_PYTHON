def single_number(nums):
    ans = 0
    for val in nums:
        ans=val^ans
    print(ans)
    

single_number([1,1,2,2,3,4,4])