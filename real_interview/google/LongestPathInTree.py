# This method gets reused in three methods below
def buildGraph(root):
	queue = collections.deque([root])
	graph = defaultdict(set)
	while queue:
		node = queue.popleft()
		for neighbor in node.children:
			queue.append(neighbor)
			graph[node.val].add(neighbor.val)
			graph[neighbor.val].add(node.val)
	return graph

# Method 1: Heap O(E + VlogV) 
from collections import defaultdict

def getLongestConsecutiveSequence(root):
	graph = buildGraph(root)

	heapOfVertices = graph.keys()
	heapq.heapify(heapOfVertices)
	lastInteger = heapq.heappop(heapOfVertices)
	sequenceSoFar = [lastInteger]
	longestPath = [lastInteger]
	
	while heapOfVertices:
		curr = heapq.heappop(heapOfVertices)
		if curr - 1 = lastInteger and lastInteger in graph[curr]:
			sequenceSoFar.append(curr)
			if len(sequenceSoFar) > len(longestPath):
				longestPath = sequenceSoFar
		else:
			sequenceSoFar = [curr]
		lastInteger = curr
	return len(longestPath)


# Method 2 : Union Find
def getLongestConsecutiveSequence(root):
	graph = buildGraph(root) 
	return len(_longestConsecutiveSeq(graph))

def _longestConsecutiveSeq(graph):

	consecutiveGroups = {}

	def find(node):
		consecutiveGroups.setdefault(node, node)

		if consecutiveGroups[node] != node:
			consecutiveGroups[node] = find(consecutiveGroups[node])

		return consecutiveGroups[node]

	def union(node1, node2):
		parent1 = find(node1)
		parent2 = find(node2)

		if parent1 != parent2:
			consecutiveGroups[parent2] = parent1

	for node1 in graph.keys():
		# If the difference is 1, then union the nodes
		if abs(graph[node1] - node1) == 1:
			union(node1, graph[node1])

	if not consecutiveGroups:
		return 1
	else:
		# Return the largest path difference between a node
		# and its absolute root parent in a consecutive group.
		return max([abs(key - val) for key, val in consecutiveGroups.items()]) + 1

# Method 3 Brute Force DFS
def getLongestConsecutiveSequence(root):
	graph = buildGraph(root)
	longest = []
	for node in graph.keys():
		sequence = _dfs(graph, {}, node)
		if len(sequence) > len(longest):
			longest = sequence
	return len(longest)

def _dfs(graph, visited, node):
	if node in visited:
		return visited[node]
	
	result = [node]
	for neighbor in graph[node]:
		if neighbor == node + 1:
			sequence = _dfs(graph, visited, neighbor)
			result.extend(sequence)
	visited[node] = result
	return result
