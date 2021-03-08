with open("Input/input7", 'r') as handle:
	content = handle.read()
content = content.split('\n')[:-1]

objects = {}
for rule in content:
	words = rule.split(' contain ')
	
	container = words[0]
	
	contained = []
	items = words[1].split(', ')
	for item in items:
		if item == 'no other bags.':	contained.append((0, 'no other bags')); break
		else:
			quantity = int(item[0])
			bag = item[2:] if item[-1] != '.' else item[2:-1]
			if quantity == 1: bag += 's'
			
			contained.append((quantity, bag))
			
	objects[container] = contained

def testKey(D, bag, key):
	"""
	Can old at least one bag inside the key bag
	"""
	if key == 'no other bags': return False

	value = D[key]
	for v in value:
		if v[1] == bag:	return True
		elif testKey(D, bag, v[1]) is True:	return True

	return False

# part 1
def searchFor(D, query):
	quantity, bag = query
	
	countContain = 0
	items = iter(D.items())
	while True:
		try:	key, value = next(items)
		except StopIteration:	break
			
		countContain += testKey(objects, query[1], key)
	return countContain

print("Shiny gold contained in",searchFor(objects, (1,'shiny gold bags')),"bags")

# part 2
def countTotal(D, key):
	if key == 'no other bags': return 1

	value = D[key]
	count = 1
	for v in value:
		count += v[0] * countTotal(D, v[1])
	return count

print("Bags required :",countTotal(objects, "shiny gold bags")-1)	
