nums=[1,2,3,4,5,6,7]
n=len(nums)
k=3
k=k%n
ans=[0]*n
p=-1*(k)
for i in range(n):
    ans[i]=nums[p+i]
for i in range(n):
    nums[i]=ans[i]
print(nums)
