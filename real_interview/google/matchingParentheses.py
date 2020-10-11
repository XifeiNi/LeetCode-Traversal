import sys
def minimumInsertToMatchTargetParentheses(base, target):
	baseIndexEnd, baseIndexStart, targetIndex = 0, 0, 0
	minInsertion = sys.maxsize
	while baseIndexStart < len(base):
		while targetIndex < len(target) and baseIndexEnd < len(base) and base[baseIndexEnd] == target[targetIndex]:
			baseIndexEnd += 1
			targetIndex += 1
		
		minInsertion = min(minInsertion, len(target) - targetIndex - 1)
		targetIndex = 0
		baseIndexStart += 1
		baseIndexEnd = baseIndexStart
	return minInsertion
			
			
