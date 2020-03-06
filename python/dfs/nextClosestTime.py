from datetime import datetime
import sys
class Solution:
    def nextClosestTime(self, time: str) -> str:
        perms = []
        minimum = sys.maxsize
        ret = ""
        nextClosest = False
        self.getPermutation(self.getTimeDigits(time), perms, [])
        for perm in perms:
            if self.toMinutes(self.constructTime(perm)) - self.toMinutes(time) > 0 and self.toMinutes(self.constructTime(perm)) - self.toMinutes(time) < minimum and self.isValid(self.constructTime(perm)):
                nextClosest = True
                ret = self.constructTime(perm)
                minimum = self.toMinutes(self.constructTime(perm)) - self.toMinutes(time)
        if not nextClosest:
            for perm in perms:
                if self.timeDiff(self.constructTime(perm), time) < minimum and self.isValid(self.constructTime(perm)):
                    ret = self.constructTime(perm)
                    minimum = self.toMinutes(self.constructTime(perm)) - self.toMinutes(time)
        return ret
            
    def getTimeDigits(self, time):
        digits = []
        for char in time:
            if char != ':':
                digits.append(char)
        return digits
    def getPermutation(self, digits, perms, toBeFormed):
        if len(toBeFormed) == 4:
            perms.append(list(toBeFormed))
            return
        for digit in digits:
            toBeFormed.append(digit)
            self.getPermutation(digits, perms, toBeFormed)
            toBeFormed.pop()
    def toMinutes(self, time):
        return int(time[:2])*60 + int(time[3:])
    def isValid(self, time):
        return int(time[:2]) <= 23 and int(time[3:]) <= 59
    def constructTime(self, digitList):
        return ''.join(digitList[:2]) + ":" + ''.join(digitList[2:])
    def timeDiff(self, time1, time2):
        if self.toMinutes(time1) - self.toMinutes(time2) < 0:
            return 1440 - self.toMinutes(time1) + self.toMinutes(time2)
        else:
            return self.toMinutes(time1) - self.toMinutes(time2)
