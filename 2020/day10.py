with open('Input/input10', 'r') as handle:
	content = handle.read().split('\n')[:-1]

vContent = [0] + [int(v) for v in content]
vContent.append(max(vContent)+3)
vContent.sort()

# part 1
j1, j3 = 0, 0
for k in range(len(vContent)-1):
	if vContent[k+1]-vContent[k] == 1:	j1 += 1
	elif vContent[k+1]-vContent[k] == 3:	j3 += 1

print("Multiplied Jolt :",j1*j3)

# part 2
def canConnect(L, noeud):
	connect = []
	for k in range(noeud-3, noeud+3):
		if k == noeud:	continue
		
		try:
			if abs(L[k]-L[noeud]) <= 3 and k >= 0:	connect.append(k)
		except IndexError:	continue
		
	return connect

paths = [canConnect(vContent,k) for k in range(len(vContent))]

def explore(L, noeud, marked):
	if noeud == len(L)-1:	return 1
	count = 0
	for neigh in L[noeud]:
		if neigh not in marked:
			count += explore(L, neigh, marked + [neigh])
	return count

print("Arrangements :", explore(paths, 0, []))
