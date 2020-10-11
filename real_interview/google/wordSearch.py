DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
def searchLongestWordInBoard(board, dictionary):
	if board is None or len(board) == 0:
		return 0
	
	trie = Trie()
	for word in dictionary:
		trie.insert(word)
	longestWordLength = 0
	for i in range(len(board)):
		for j in range(len(board[0])):
			if not trie.startsWith(board[i][j]):
				continue
			result = set()
			_dfs(i, j, board, trie, board[i][j], set(), result)
			longestWordLength = max(max(len(word) for word in result), longestWordLength)
	return longestWordLength

def _dfs(x, y, board, trie, word, visited, result):
	if word is None:
		return
	
	if trie.find(word):
		result.add(word)
	
	for deltaX, deltaY in DIRECTIONS:
		nextX, nextY = x + deltaX, y + deltaY
		if not inside(nextX, nextY, board) or (nextX, nextY) in visited or not trie.startsWith(word + board[nextX][nextY]):
			continue
		visited.add((nextX, nextY))
		_dfs(nextX, nextY, trie, word + board[nextX][nextY], visited, result)
		visited.remove((nextX, nextY))
	

def inside(x, y, board):
	return 0 <= x < len(board) and 0 <= y < len(board[0])
		
