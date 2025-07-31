def max_subarray(nums):
    csum =0
    msum=-(2**31)
    for item in nums:
        if csum<0:
            csum=0
        csum+=item
        msum=max(csum,msum)
    print(msum)

max_subarray([-2,1,-3,4,-1,2,1,-5,4])