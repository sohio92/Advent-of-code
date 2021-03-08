with open("Input/input4", 'r') as handle:
	content = handle.read()[:-1]

def listInList(A, B):
	for a in A:
		if a not in B:	return False
	return True

def inRange(values, lows, highs):
	for k in range(len(values)):
		if not(int(values[k]) >= lows[k] and int(values[k]) <= highs[k]):
			return False
	return True 
	
listIndiv = [{}]
for line in content.split('\n'):
	if len(line) == 0: 
		listIndiv.append({})
		continue
	
	lChar = line.split(' ')
	for char in lChar:
		keyValue = char.split(':')
		listIndiv[-1][keyValue[0]] = keyValue[1]

# part 1
mandatory, optional = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], ['cil']
valids = []
for indiv in listIndiv:
	if listInList(mandatory, indiv.keys()):
		valids.append(indiv)

print("Valid :", len(valids))

# part 2
countValid = 0
for indiv in valids:
	if inRange([indiv['byr'], indiv['iyr'], indiv['eyr']], [1920, 2010, 2020], [2002, 2020, 2030]):
		hgt = indiv['hgt']
		if (hgt[-2:] == 'cm' and inRange([hgt[:-2]], [150], [193])) or (hgt[-2:] == 'in' and inRange([hgt[:-2]], [59], [76])):
			hcl = indiv['hcl']
			if hcl[0] == '#' and len(hcl) == 7 and listInList(hcl[1:], "0123456789abcdef"):
				if indiv['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
					pid = indiv['pid']
					if len(pid) == 9 and listInList(pid, "0123456789"):
						countValid += 1

print("Valid :", countValid)
