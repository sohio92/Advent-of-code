with open("Input/input2", 'r') as handle:
	content = handle.readlines()

# part 1
countValid = 0
for line in content[:-1]:
	lim, letter, word = line.split(" ")
	
	low, high = map(int, lim.split('-'))
	letter = letter[0]
	word = word[:-1]
	
	countLetter = 0
	for l in word:
		if letter == l: countLetter +=1
	
	if countLetter in range(low, high+1): countValid += 1

print("Valid :", countValid)

# part 2
countValid = 0
for line in content[:-1]:
	lim, letter, word = line.split(" ")
	
	low, high = map(int, lim.split('-'))
	letter = letter[0]
	word = word[:-1]
	
	ww = word[low-1] + word[high-1]
	if letter in ww and 2*letter != ww: countValid += 1

print("Valid :", countValid)
	
