class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start:int, end:int, nums:List[int] )->int:
            if end < start:
                return -1
            mid = start + (end-start)//2
            if nums[mid]==target:

                return mid
            if nums[mid]>target:
                return binary_search(start,mid-1,nums)
            else:   
                return binary_search(mid+1,end,nums) 
        return binary_search(0,len(nums)-1,nums)
            
        