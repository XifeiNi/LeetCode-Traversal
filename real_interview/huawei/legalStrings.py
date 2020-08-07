

STRING_PREFIX_1 = "0X01"
STRING_PREFIX_2 = "0X02"
STRING_PREFIX_3 = "0X03"
from collections import defaultdict
# import assert
STRING_PREFIX_LIST = [STRING_PREFIX_1, STRING_PREFIX_2, STRING_PREFIX_3]
def legalStrings(stringList):
	if (stringList is None):
		return []	
	ret = defaultdict(int) 	# Map/ dict
	end = 0
	temp = []
	while end < len(stringList):
		if stringList[end] not in STRING_PREFIX_LIST:
			temp.append(stringList[end])
			end += 1
			ret["+".join(temp)] += 1
			temp = []
		else:
			temp.append(stringList[end])
			end += 1
	return reversed(sorted(lambda x: ret[x], ret))
# [ "OX021", "0X012", "0X0X0X03A"]
# IO
# 从本地读取input

# unit test
TEST1 = []
TEST2 = ["OXO2" ,"1"]
print(legalStrings(TEST1))

				
