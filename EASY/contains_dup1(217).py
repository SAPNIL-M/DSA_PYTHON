def containsDuplicate(nums):

    hset = set()
    for num in nums:  
        if num in hset:
            return True 
        else:
            hset.add(num)
    return False  


"""test cases written using ai"""
nums1 = [1, 2, 3, 1]
print(f"Does {nums1} contain duplicates? {containsDuplicate(nums1)}")

nums2 = [1, 2, 3, 4]
print(f"Does {nums2} contain duplicates? {containsDuplicate(nums2)}")

nums3 = []
print(f"Does {nums3} contain duplicates? {containsDuplicate(nums3)}")

nums4 = [1]
print(f"Does {nums4} contain duplicates? {containsDuplicate(nums4)}")