class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        target_seen = set()
        dup = dict()
        dup_zero = set()
        for i in range(len(nums)):
            if nums[i] in target_seen:
                continue
            target_seen.add(nums[i])
            target_set = set()
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] in target_set:
                    tmp_result = nums[i] * nums[j] * (-nums[i]-nums[j])
                    if tmp_result:
                        if tmp_result in dup and (nums[i] in dup[tmp_result] or nums[j] in dup[tmp_result] or (-nums[i]-nums[j]) in dup[tmp_result]):
                            continue
                        else:
                            result.append(sorted([-nums[i]-nums[j], nums[i], nums[j]]))
                            if tmp_result in dup :
                                dup[tmp_result].add(nums[i])
                            else:
                                dup[tmp_result] = {nums[i]}
                    else:
                        if nums[i] == 0:
                            if nums[j] * (-nums[i]-nums[j]) in dup_zero:
                                continue
                            else:
                                dup_zero.add(nums[j] * (-nums[i]-nums[j]))
                        elif nums[j] == 0:
                            if nums[i] * (-nums[i]-nums[j]) in dup_zero:
                                continue
                            else:
                                dup_zero.add(nums[i] * (-nums[i]-nums[j]))
                        elif -nums[i]-nums[j] == 0:
                            if nums[i] * nums[j] in dup_zero:
                                continue
                            else:
                                dup_zero.add(nums[i] * nums[j])
                        result.append(sorted([-nums[i]-nums[j], nums[i], nums[j]]))
                else:
                    target_set.add(-nums[i]-nums[j])
        return sorted(result)