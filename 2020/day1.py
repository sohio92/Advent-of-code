content = []
with open("Input/input1", 'r') as handle:
	while True:
		try:	content.append(int(handle.readline()))
		except:	break

def findSum(A, value):
	for k in range(len(A)):
		search = value - A[k]
		for l in A[:k] + A[k+1:]:
			if l == search:	return(A[k],l)
	return None, None

a,b = findSum(content,2020)
print("{} * {} = {}".format(a,b,a*b))

for k in range(len(content)):
	search = 2020 - content[k]
	a, b = findSum(content[:k]+content[k+1:], search)
	
	if a is not None:
		print("{} * {} * {} = {}".format(content[k], a, b, content[k] * a * b))
		break
	
	
