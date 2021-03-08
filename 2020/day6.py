with open("Input/input6", 'r') as handle:
	content = handle.read()
content = content.split('\n')[:-1]

groups = [[]]
for line in content:
	if len(line) == 0:
		groups.append([])
		continue
	
	groups[-1].append(line)

# part 1
nLetters = 0
for group in groups:
	letters = []
	for indiv in group:
		for letter in indiv:
			if letter not in letters: letters.append(letter)
	nLetters += len(letters)

print("Sum of count :",nLetters)
	
# part 2
nLetters = 0
for group in groups:
	letters = {}
	for indiv in group:
		for letter in indiv:
			if letter not in letters.keys(): letters[letter] = 0
			letters[letter] += 1
	
	for value in letters.values():
		if value == len(group):	nLetters += 1

print("Sum of count :",nLetters)
