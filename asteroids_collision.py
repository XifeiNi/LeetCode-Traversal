class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack, i = [], 0
        while i < len(asteroids):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            elif len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroids[i])
            elif len(stack) > 0 and stack[-1] <= -asteroids[i]:
                if stack[-1] < -asteroids[i]:
                    i-=1
                stack.pop()
            i+=1
        return stack
                
