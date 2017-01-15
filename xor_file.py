#!/usr/bin/python
import sys
if len(sys.argv) != 5: 
	print "Usage: ./xor_file infile outfile key offset"
	exit()

def xor_data(data, key):
	l = len(key)
	decoded = ""
	for i in range(0, len(data)):
		decoded += chr(data[i]^ord(key[i%l]))
	return decoded
	
f = open(str(sys.argv[1]), "rb")
g = open(str(sys.argv[2]), "wb")
key = sys.argv[3]
len_key = len(sys.argv[3])
offset = int(sys.argv[4])
iter = 0
try:
	print( "offset = "+str(offset))
	f.seek(offset)
	aPiece = f.read(len_key)
	while aPiece != "":
		for i in range (0, len(aPiece)):
			g.write(chr(ord(aPiece[i])^ord(key[i])))
		print(aPiece+" | ")
		aPiece = f.read(len_key)
finally:
	f.close()
g.close()











