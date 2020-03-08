from functools import reduce
from sys import setrecursionlimit

setrecursionlimit(100000)

up = 'U'
down = 'D'
left = 'L'
right = 'R'
directions = [up, down, left, right]
reversed_direction = {up: down, down: up, left: right, right: left}

rows, cols = map(int, input().split())
gridarr = [list(map(int, input().split())) for i in range(rows)]
r, c = map(lambda x: int(x) - 1, input().split())

def grid(x, y=None):
	global gridarr
	if y == None:
		x, y  = x
	return gridarr[y][x]

def setgrid(val, x, y=None):
	global gridarr
	if y == None:
		x, y = x
	gridarr[y][x] = val

def car(p):
	if grid(p) < 0:
		return (p, None)
	return list(filter(lambda x: grid(p) == grid(x[0]), otherdir(p)))[0]

def adj(p, d):
	x, y = p
	if d == up:
		return (x,y-1)
	elif d == down:
		return (x,y+1)
	elif d == left:
		return (x-1,y)
	elif d == right:
		return (x+1,y)

def oob(p):
	x, y = p
	return x < 0 or x >= cols or y < 0 or y >= rows

def findempty():
	for i in range(rows):
		for j in range(cols):
			if grid(j,i) == -1:
				return (j,i)

def moveinempty(p, cardir):
	car = adj(adj(p, cardir), cardir)
	carval = grid(car)
	setgrid(carval,p)
	setgrid(-1,car)
	return car

def otherdir(p):
	return [(adj(p, direc), direc) for direc in directions if not oob(adj(p,direc))]

def dfs(p, notcar):
	if grid(c,r) == -1:
		return (True, [])
	carpos = filter(lambda x: x[1] == car(x[0])[1] and grid(car(x[0])[0]) != notcar, otherdir(p))
	cars = map(lambda x: car(x[0]), carpos)
	pathfound = False
	shortestlength = float("inf")
	shortestpath = []
	for i in cars:
		carval = grid(i[0])
		empty = moveinempty(p, i[1])
		found, path = dfs(empty, carval)
		pathfound |= found
		if found and len(path) + 1 < shortestlength:
			shortestpath = [carval] + path
		moveinempty(empty, reversed_direction[i[1]])
	return pathfound, shortestpath

found = None
ans = []
initial = findempty()
found, ans = dfs(initial, -3)
if found == True:
	print(reduce(lambda x, y: str(x) + " " + str(y), ans[1:], ans[0]))
elif found == False:
	print('impossible')
