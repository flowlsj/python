appleProducts = ['iPhone', 'iPad', 'iPod', 'iTouch', 'iWatch']
print 'Apple\'s products are:', appleProducts
print 'There are', len(appleProducts), 'products so far'

phone = appleProducts[1]
print 'Apple\'s pad is:', phone

del appleProducts[1]
print 'Besides ipad, there are', len(appleProducts), 'products'
print 'They are', appleProducts

print 'Oh, I forgot iMac, let\'s add it'
appleProducts.append('iMac')

print 'Now the products list is:'
for item in appleProducts:
	print item,

print '\nNow let\' sort the list'
appleProducts.sort()
for item in appleProducts:
	print item,
