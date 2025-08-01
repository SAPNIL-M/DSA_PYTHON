from collections import defaultdict
def two_sum(nums,target):
    hmap=defaultdict(int)
    for i,val in enumerate(nums):
        if target-val in hmap:
            return[i,hmap[target-val]]
        else:
            hmap[val]=i
    
print(two_sum([2,7,11,15],9))