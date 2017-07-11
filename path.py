#Author: Bailey Morris 
#ID: 8251672

def main():
	while True:
		try:
			graphunsorted = {}
			order = int(input())
		except EOFError:
			break
		if order == 0:
			break
		for i in range(order):
			graphunsorted[i] = input().strip().split()
		print(findlongestpath(graphunsorted))

def indegreesCalc(graph):
	#find the indegrees of each node in the graph, helps with topo sort
	indegrees = {}
	for i in range(len(graph)):
		indegrees[i] = 0
	for u in range(len(graph)):
		for v in graph[u]:
			indegrees[int(v)] += 1
	return indegrees


def toposort(graphunsorted):
	#topologically sort the graph, done before finding the longest path
	indegrees = indegreesCalc(graphunsorted)
	graphsorted = []
	stack = []

	for i in range(len(indegrees)):
		if indegrees[i] == 0:
			stack.append(i)

	while stack:
		node = stack.pop()
		graphsorted.append(node)

		if len(graphunsorted[node]) == 0:
			continue
		else:
			for n in graphunsorted[node]:
				i = int(n)
				indegrees[i] -= 1
				if indegrees[i] == 0:
					stack.append(i)
	return graphsorted

def findlongestpath(graph):
	graphsorted = toposort(graph)
	dist = {}
	for i in range(len(graphsorted)):
		dist[i] = -99999999
	dist[0] = 0;

	for u in graphsorted:
		for v in graph[u]:
			if dist[int(v)] < ((dist[u]) + 1):
				dist[int(v)] = ((dist[u]) + 1)
	try:
		return max(dist[i] for i in range(len(graphsorted)))
	except ValueError:		#if no adjacent vertices for vertex 0
		return 0

main()