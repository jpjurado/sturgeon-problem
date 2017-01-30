from wheel import Wheel

DICT = '2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7'
PATH_TEXT = 'part_2/plaintext.txt'
PATH_CIPHER = 'part_2/ciphertext.txt'

wheel_47 = Wheel(47)
wheel_47.set(0,1)

wheels = [
	Wheel(47),
	Wheel(53),
	Wheel(59),
	Wheel(61),
	Wheel(64),
	Wheel(65),
	Wheel(67),
	Wheel(69),
	Wheel(71),
	Wheel(73),
]

print wheels[0].getTotal(),wheels[1].size

file_object  = open(PATH_TEXT, 'r')
print DICT.index('T')


for line in file_object.readlines():
	for char in line:
		try:
			alph = DICT.index(char)
			message.append(alph)
		except:
			break

def parseText(path):
	message = []
	file_object  = open(path, 'r')
	for line in file_object.readlines():
		for char in line:
			try:
				alph = DICT.index(char)
				message.append(alph)
			except:
				break
	return message

def encryp_xor(wheels,value):
	data = intToArray(value)
	for index,val in enumerate(data):
		#print index,val,wheels[index],val ^ wheels[index]
		data[index] = val ^ wheels[index]
	return [arrayToInt(data),data]

def arrayToInt(array):
	number = ''
	for bit in array:
		number = number + str(bit)
	return int(number,2)

def intToArray(num):
	array = []
	bits = "{0:05b}".format(num)
	for bit in bits:
		array.append(int(bit))
	return array

def getCurrentValues(pos):
	current_weels = []
	for wheel in wheels:
		current_weels.append(wheel.get(pos))
	return current_weels


plain_message = parseText(PATH_TEXT)
cipher_message = parseText(PATH_CIPHER)

print len(plain_message)
print len(cipher_message)
for index,value in enumerate(cipher_message):
	if value == 0 or value == 31:
		bits = "{0:05b}".format(plain_message[index])
		for index_bit,bit in enumerate((bits)):
			if value == 0:
				val = int(bit)
			else:
				val = int(bit) ^ 1
			if wheels[index_bit].exist(index):
				#print val,wheels[index_bit].get(index)
				if val != wheels[index_bit].get(index):
					print 'No coinciden',plain_message[index],val,wheels[index_bit].get(index)
					print value,bits,index_bit,bit
			else:
				wheels[index_bit].set(index,val)	



set_cero = [0b10111,0b11011,0b11101]
set_one = [0b01000,0b00100,0b00010]

cont = 0
for index,value in enumerate(cipher_message):
	[encrypt,encrypt_bits] = encryp_xor(getCurrentValues(index),plain_message[index])
	if encrypt in set_cero:
		cont = cont + 1
		index_message = encrypt_bits.index(0)
		index_sturgeon = intToArray(value).index(0)
		if index_message == index_sturgeon:
			wheels[5+index_message].set(index,0)
			wheels[5+index_sturgeon].set(index,0)
		elif index_sturgeon < index_message:
			wheels[5+index_message].set(index,1)
		else:
			for index_wheel in range(index_message+1,index_sturgeon+1):
				wheels[5+index_wheel].set(index,1)
		#print 'Set cero','Result: ',encrypt_bits,intToArray(value),index_message,index_sturgeon
	elif encrypt in set_one:
		cont = cont + 1
		index_message = encrypt_bits.index(1)
		index_sturgeon = intToArray(value).index(1)
		if index_message == index_sturgeon:
			wheels[5+index_message].set(index,0)
			wheels[5+index_sturgeon].set(index,0)
		elif index_sturgeon < index_message:
			wheels[5+index_message].set(index,1)
		else:
			for index_wheel in range(index_message+1,index_sturgeon+1):
				wheels[5+index_wheel].set(index,1)
		#print 'Set one','Result: ',encrypt_bits,intToArray(value),index_message,index_sturgeon
	if value == 0b10000:
		index_message = encrypt_bits.index(1)
		index_sturgeon = intToArray(value).index(1)
		if index_message == index_sturgeon:
			wheels[5].set(index,0)
			wheels[6].set(index,0)
		elif index_message == 4:
			wheels[5].set(index,1)
			wheels[6].set(index,0)
			print 'Start one','Result: ',getCurrentValues(index)
		#print encrypt_bits,intToArray(value),index_message,index_sturgeon
	elif value == 0b01111:
		index_message = encrypt_bits.index(0)
		index_sturgeon = intToArray(value).index(0)
		if index_message == index_sturgeon:
			wheels[5].set(index,0)
			wheels[6].set(index,0)
		elif index_message == 4:
			wheels[5].set(index,1)
			wheels[6].set(index,0)
		"""
		else:
			print 'Set one','Result: ',getCurrentValues(index)
			print encrypt_bits,intToArray(value),index_message,index_sturgeon
			print 'Index',index_sturgeon
		"""
		#print encrypt_bits,intToArray(value),index_message,index_sturgeon


print 'Cont',cont
cont = 0

set_cero = [0b01111,0b11110]
set_one =  [0b10000,0b00001]

for index,value in enumerate(cipher_message):
	[encrypt,encrypt_bits] = encryp_xor(getCurrentValues(index),plain_message[index])
	if None in getCurrentValues(index):
		if encrypt in set_cero:
			index_message = encrypt_bits.index(0)
			index_sturgeon = intToArray(value).index(0)
			cont = cont + 1
			print 'Set cero','Result: ',getCurrentValues(index)
			print encrypt_bits,intToArray(value),index_message,index_sturgeon
		if encrypt in set_one:
			index_message = encrypt_bits.index(1)
			index_sturgeon = intToArray(value).index(1)
			cont = cont + 1
			print 'Set one','Result: ',getCurrentValues(index)
			print encrypt_bits,intToArray(value),index_message,index_sturgeon

print 'Cont',cont

print wheels[0].size,wheels[0].getTotal()
print wheels[1].size,wheels[1].getTotal()
print wheels[2].size,wheels[2].getTotal()
print wheels[3].size,wheels[3].getTotal()
print wheels[4].size,wheels[4].getTotal()
print wheels[5].size,wheels[5].getTotal()
print wheels[6].size,wheels[6].getTotal()
print wheels[7].size,wheels[7].getTotal()
print wheels[8].size,wheels[8].getTotal()
print wheels[9].size,wheels[9].getTotal()