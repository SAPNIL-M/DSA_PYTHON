def missing_num(nums):
    
    n=len(nums)
    sumn=n*(n+1)/2
    sumnums=sum(nums)
    print(int(sumn-sumnums))
    return 0

missing_num([3,0,1])