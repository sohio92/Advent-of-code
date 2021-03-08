with open("Input/input5", 'r') as handle:
	content = handle.read()
content = content.split('\n')[:-2]

ids = []
for line in content:
	sRow = line[:7]
	sCol = line[7:]
	
	lRow = list(range(128))
	lCol = list(range(8))
	for r in sRow:
		if r == 'B': lRow = lRow[int(len(lRow)/2):]
		else:	lRow = lRow[:int(len(lRow)/2)]
		
	for c in sCol:
		if c == 'R': lCol = lCol[int(len(lCol)/2):]
		else:	lCol = lCol[:int(len(lCol)/2)]
	
	ids.append(lRow[0]*8+lCol[0])

# part 1
print("Highest seat ID :",max(ids))

# part 2
for k in range(len(ids)):
	for seat2 in ids[:k] + ids[k+1:]:
		if seat2 == ids[k] + 2:
			if seat2-1 not in ids: mySeat = seat2-1

print("My seat :", mySeat)
