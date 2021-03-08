with open('Input/input8', 'r') as handle:
	content = handle.read().split('\n')[:-1]

# part 1
def doesLoop(C):
	visited = []
	acc = 0
	k = 0
	while k < len(C):
		if k in visited:	return (True, k, acc)
		visited.append(k)
		
		try:	ins, num = C[k].split(' ')
		except IndexError:	return (True, k, acc)
		
		if ins == 'nop':	pass
		elif ins == 'acc':	acc += int(num)
		elif ins == 'jmp':	k += int(num); continue
		
		k += 1
	return (False, None, acc)

print("Value in the accumulator :", doesLoop(content)[-1])

# part 2
k = 0
visited = []
acc = 0
while k < len(content):
	if k in visited:	break
	visited.append(k)
	ins, num = content[k].split(' ')
	if ins == 'nop':
		res = doesLoop(content[:k] + ['jmp' + content[k][3:]] + content[k+1:])
		if res[0] is False:	acc = res[-1];	break
	elif ins =='acc':	acc += int(num)
	elif ins == 'jmp':
		res = doesLoop(content[:k] + ['nop' + content[k][3:]] + content[k+1:])
		if res[0] is False:	acc = res[-1];	break
		k += int(num)
		continue
	
	k += 1

print("Value in the accumulator :", acc)
	
