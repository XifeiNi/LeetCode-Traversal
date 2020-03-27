class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
        if len(v1) > len(v2):
            for i in range(min(len(v1), len(v2)), len(v1)):
                if int(v1[i]) != 0:
                    return 1
        if len(v2) > len(v1):
            for i in range(min(len(v1), len(v2)), len(v2)):
                if int(v2[i]) != 0:
                    return -1
        return 0
