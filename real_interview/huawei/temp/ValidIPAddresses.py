
LEN_VALID_IP = 4
NON_VALID_START = '0'
MAX_IP_NUM = 255
def getNumValidIPAddresses(string):
	if string is None or len(string) == 0:
		return 0
	ipNumList = string.split('.')
 	start, end = 0, LEN_VALID_IP - 1

	visitedIPAddresses = set()
	while end < len(ipNumList):
		addValidIPs(start, end, ipNumList, visitedIPAddresses)		
		start+=1
		end+=1
	return len(visitedIPAddresses)
def addValidIPs(start, end, stringList, visitedIPAddresses):
	if not isValidIP(start, end, stringList):
		return	
	validString = '.'.join(stringList[start:end+1])
	for windowStart in range(0, len(stringList[start]))
		for windowEnd in range(0, len(stringList[end])):
			visitedIPAddresses.add(validString[windowStart: windowEnd])
	return
def isValidIP(start, end, stringList):
	initialStart = start
	while start < end:
		for index in len(0, len(stringList[start]):
			if (index != 0 and not stringList[start][index].isNumber()):
				return False
		if start != initialStart and start != end and int(stringList[start]) > MAX_IP_NUM:
			return False
		if start != initialStart and stringList[start][0] == NON_VALID_START:
			return False
	return True
	
