class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        hashMap = {}
        results = []
        for num in nums2:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num]+=1
        
        for num in nums1:
            if num in hashMap and hashMap[num] >= 1:
                hashMap[num]-=1
                results.append(num)
        return results
