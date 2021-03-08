content = []
with open("Input/input3", 'r') as handle:
	while True:
		line = handle.readline()
		if len(line) == 0: break
		content.append(line[:-1])

def getTree(A, slope):
	position = 0
	countTree = 0
	for k in range(0,len(A),slope[1]):
		try:
			if A[k][position] == '#':	countTree += 1
		except IndexError:	break
		
		position += slope[0]
		position %= len(A[0])

	return countTree
	
print("Number of trees :", getTree(content, (3,1)))

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
p = 1
for slope in slopes:
	p*=getTree(content, slope)

print("Multiplied :", p)
	
