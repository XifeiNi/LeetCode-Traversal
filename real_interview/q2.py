
def first(price, numProduct):
	ret=0
	thirteen=price//13

	ret+=min(thirteen, numProduct[4])
	price = price - min(thirteen, numProduct[4])*13

	eleven=price//11
	ret+=min(eleven, numProduct[3])
	price = price - min(eleven, numProduct[3])*11

	seven=price//7
	ret+=min(seven, numProduct[2])
	price = price - min(seven, numProduct[2])*7

	three=price//3
	ret+=min(three, numProduct[1])
	price = price - three * min(three, numProduct[1])
	if price > numProduct[0]:
		return 10000

	ret+=price
	return ret
def second(price, numProduct):
	ret=0

	eleven=price//11
	ret+=min(eleven, numProduct[3])
	price = price - min(eleven, numProduct[3])*11

	thirteen=price//13
	ret+=min(thirteen, numProduct[4])
	price = price - min(thirteen, numProduct[4])*13

	seven=price//7
	ret+=min(seven, numProduct[2])
	price = price - min(seven, numProduct[2])*7

	three=price//3
	ret+=min(three, numProduct[1])
	price = price - three * min(three, numProduct[1])
	if price > numProduct[0]:
		return 10000

	ret+=price
	return ret
def third(price, numProduct):
	ret=0

	seven=price//7
	ret+=min(seven, numProduct[2])
	price = price - min(seven, numProduct[2])*7

	eleven=price//11
	ret+=min(eleven, numProduct[3])
	price = price - min(eleven, numProduct[3])*11

	thirteen=price//13
	ret+=min(thirteen, numProduct[4])
	price = price - min(thirteen, numProduct[4])*13


	three=price//3
	ret+=min(three, numProduct[1])
	price = price - three * min(three, numProduct[1])
	if price > numProduct[0]:
		return 10000

	ret+=price
	return ret
def fourth(price, numProduct):
	ret=0


	seven=price//7
	ret+=min(seven, numProduct[2])
	price = price - min(seven, numProduct[2])*7

	thirteen=price//13
	ret+=min(thirteen, numProduct[4])
	price = price - min(thirteen, numProduct[4])*13

	eleven=price//11
	ret+=min(eleven, numProduct[3])
	price = price - min(eleven, numProduct[3])*11

	three=price//3
	ret+=min(three, numProduct[1])
	price = price - three * min(three, numProduct[1])
	if price > numProduct[0]:
		return 10000

	ret+=price
	return ret
data=map(int, input().strip().split())
numProduct=[]
numProduct.extend(data)
price=int(input())
strategies=[first(price, numProduct), second(price, numProduct), third(price, numProduct), fourth(price, numProduct)]
ret=min(strategies)
print(ret)