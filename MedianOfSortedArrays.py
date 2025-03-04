#Time Complexity: O(log(m+n))
#Space Complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if n<m:
            return self.findMedianSortedArrays(nums2,nums1)
        low = 0
        high = m
        while low<=high:
            partX = (low+high)//2
            partY = (m+n)//2 - partX
            L1 = float('-inf') if partX==0 else nums1[partX-1]
            L2 = float('-inf') if partY==0 else nums2[partY-1]
            R1 = float('inf') if partX==m else nums1[partX]
            R2 = float('inf') if partY==n else nums2[partY]
            if L1<=R2 and L2<=R1:
                if (m+n)%2!=0:
                    return min(R1,R2)
                else:
                    return (max(L1,L2)+min(R1,R2))/2
            elif L2>R1:
                low = partX+1
            else:
                high = partX-1