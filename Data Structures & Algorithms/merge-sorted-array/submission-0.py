class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

 


        for i, num in enumerate(nums2):
            nums1[m+i] = num
            currIdx = m+i
            while (currIdx > 0):
                if nums1[currIdx] >= nums1[currIdx - 1]:
                    break;
                else:
                    temp = nums1[currIdx - 1]
                    nums1[currIdx - 1] = nums1[currIdx]
                    nums1[currIdx] = temp
                currIdx -= 1; 




        