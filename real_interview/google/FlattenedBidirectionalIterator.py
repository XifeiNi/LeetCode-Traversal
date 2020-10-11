
class FlattenedBidirectionalIterator:
	def __init__(iterators):
		self.iterators = iterators
		self.whichIterator = 0
	
	def next():
		if not self.hasNext():
			return None
		nextIndex = self._getIteratorIndex(True)
		return self._getElementByIteratorIndex(nextIndex, True)
	
	def hasNext():
		for i in range(0, len(self.iterators):
			if self.iterators[i].hasNext():
				return True
		return False
	
	def previous():
		if not self.hasPrevious():
			return None
		previousIndex = self._getIteratorIndex(False)
		return self._getElementByIteratorIndex(nextIndex, False)
	
	def hasPrevious():
		for i in range(0, len(self.iterators):
			if self.iterators[i].hasPrevious():
				return True
		return False
		
	def _getIteratorIndex(flag):
		ret =  (self.whichIterator) % len(self.iterators)
		if flag:
			self.whiciIterator += 1
		else:
			self.whiciIterator -= 1
		return ret
			
	def _getElementByIteratorIndex(index, flag):
		if flag and self.interators[index].hasNext():
			return  self.interators[index].next()
		elif not flag and self.interator[index].hasPrevious():
			return self.interators[index].previous()
		else:
			self.whiciIterator = self._getIteratorIndex(flag)
			param = self.whichIterator
			return self._getElementByIteratorIndex(param, flag)
