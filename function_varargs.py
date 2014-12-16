def sum(a=10, *number, **keywords):
	total = a
	for n in number:
		total += n
	for key in keywords:
		total += keywords[key]
	return total

print sum(3,4,5,6, vnx=30, vnxe=15)
