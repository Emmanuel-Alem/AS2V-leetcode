class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = []
        s = []
        d = []
        for i in range(len(nums)-n):
            l.append(nums[i])
        for i in range(len(nums)-n,len(nums)):
            s.append(nums[i])
        for i in range(len(l)):
            d += l[i],s[i]
            
        return d
