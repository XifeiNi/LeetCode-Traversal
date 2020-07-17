
def englishRules(string):
	word_list = string.split(' ')
	preceding, succeeding = set(), set()
	nochange = 1
	while nochange==1:
		nochange=0
		for i in range(len(word_list)):
			if word_list[i][-1] == ',':
				succeeding.add(word_list[i][0:-1])
				if i + 1 < len(word_list):
					preceding.add(word_list[i+1])
		print(preceding)
		print(succeeding)
		for i in range(len(word_list)):
			if word_list[i] in preceding:
				if i - 1 >= 0 and word_list[i-1][-1] != ',' and word_list[i-1][-1] != '.':
					word_list[i-1] = word_list[i-1] + ','
					nochange=1
			if word_list[i] in succeeding:
				if word_list[i-1][-1] != ',' and word_list[i-1][-1] != '.':
					word_list[i] = word_list[i] + ','
					nochange=1

	return ' '.join(word_list)
if __name__ == '__main__':
	s = input()
	print(englishRules(s))
