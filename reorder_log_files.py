class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs, letterLogs = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        letterLogs = sorted(letterLogs,key = lambda a:(a.split(' ')[1::],a.split(' ')[0]))
        return letterLogs + digitLogs
