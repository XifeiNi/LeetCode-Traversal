class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushIndex, popIndex = 0, 0
        for push in pushed:
            pushed[pushIndex] = push
            while pushIndex >= 0 and pushed[pushIndex] == popped[popIndex]:
                pushIndex -= 1
                popIndex += 1
            pushIndex += 1
        return pushIndex == 0
