'''
This is a program to test pickle module
'''
import pickle

appleProducts = ['iMac', 'iPad', 'iPhone']

#open a file to serilize the appleProducts
f = open('apple.data', 'wb')
pickle.dump(appleProducts, f)
f.close()

del appleProducts

f = open('apple.data', 'rb')
storedProducts = pickle.load(f)
print storedProducts
