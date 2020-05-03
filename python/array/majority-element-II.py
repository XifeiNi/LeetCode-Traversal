class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = []
        key1, counter1, key2, counter2 = None, 0, None, 0
        for num in nums:
            
            if num == key1:
                counter1 += 1
            elif num == key2:
                counter2 += 1
            elif counter1 == 0:
                key1 = num
                counter1 += 1
            elif counter2 == 0:
                key2 = num
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == key1:
                cnt1 += 1
            if num == key2:
                cnt2 += 1
        if cnt1 > n // 3:
            ret.append(key1)
        if cnt2 > n // 3:
            ret.append(key2)
        return ret
        
