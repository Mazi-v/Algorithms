class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Define the merge function to merge two sorted lists
        def merge(l: List[int], r: List[int], nums: List[int]) -> List[int]:
            i, j, k = 0, 0, 0
            
            # Compare elements in the left and right lists and merge them in ascending order
            while i < len(l) and j < len(r):
                if l[i] >= r[j]:
                    nums[k] = r[j]
                    j += 1
                else:
                    nums[k] = l[i]
                    i += 1
                k += 1
            
            # If there are remaining elements in the left or right list, append them to the result
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1
            
            return nums
        
        # Base case: if the list has one or zero elements, it is considered sorted
        if len(nums) < 2:
            return nums
        
        # Divide the list into two halves
        m = len(nums) // 2
        l = nums[:m]
        r = nums[m:]
        
        # Recursively sort the left and right halves
        self.sortArray(l)
        self.sortArray(r)
        
        # Merge the sorted halves to produce the final sorted list
        return merge(l, r, nums)