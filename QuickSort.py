class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Partition function that arranges elements such that elements less than the pivot
        # are on the left and elements greater than the pivot are on the right.
        def partition(nums: List[int], start: int, end: int) -> int:
            j = start - 1
            pivot = nums[end]  # Choose the last element as the pivot
            for i in range(start, end):
                if nums[i] < pivot:
                    j += 1
                    # Swap elements to move smaller elements to the left
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
            j += 1
            # Swap the pivot element to its correct position
            temp = nums[j]
            nums[j] = pivot
            nums[end] = temp
            return j  # Return the pivot index

        # QuickSort function that recursively sorts the elements in the array.
        def quicksort(nums: List[int], start: int, end: int):
            if end <= start:
                return
            pivot = partition(nums, start, end)  # Find the pivot index
            # Recursively sort the left and right subarrays
            quicksort(nums, start, pivot - 1)
            quicksort(nums, pivot + 1, end)

        start = 0  # Starting index
        end = len(nums) - 1  # Ending index
        quicksort(nums, start, end)  # Call the QuickSort function to sort the array
        return nums  # Return the sorted array