with open('Input/input9', 'r') as handle:
	content = handle.read().split('\n')[:-1]

def sumPrevious(L, number):
	S = []
	for v1 in L:
		for v2 in L:
			S.append(v1+v2)
	return number in S

# part 1
vContent = [int(k) for k in content]
num, indice = None, None
for k in range(25,len(content)):
	if sumPrevious(vContent[k-25:k], vContent[k]) is False:	num, indice = vContent[k], k; break

print("First invalid :", num)

# part 2
def findRange(L, number, ind):
	low, high = None, None
	for l in range(ind):
		for h in range(l+1, ind):
			nRange = L[l:h+1]
			if number == sum(nRange):	low, high = min(nRange), max(nRange);	return low + high

print("Encryption weakness :", findRange(vContent, num, indice))
