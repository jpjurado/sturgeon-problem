from wheel import Wheel

DICT = '2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7'
PATH_TEXT = 'part_1/plaintext.txt'
PATH_CIPHER = 'part_1/ciphertext.txt'


wheels = [
	Wheel(data='10100110111100011011010011011111111100111111000010011111100110001110111',offset=44),
	Wheel(data='100111110011101001010100000011111110110100010111011110001110000011010',offset=52),
	Wheel(data='00001011011010001001100011001000101000001001101111110100011',offset=35),
	Wheel(data='1111000110101001011110010001001100000101111110111110001011010010',offset=14),
	Wheel(data='0110111001111011100111011111101001110011101100101001100011100',offset=19),
	Wheel(data='11111111110010110011010010011001011000101011010011010110101001010',offset=55),
	Wheel(data='1010110101100010100100100101010111000100110011110010100100111100110',offset=6),
	Wheel(data='11110001110100111111010101111100101000011110010010000',offset=4),
	Wheel(data='11000011010111101011100011111101111011110110010',offset=3),
	Wheel(data='0101011101110100010011000111101110011010001111101111100110000000101101111',offset=51)
]

def encryp(wheels,data):
	print 'Wheels',wheels,data
	for index,val in enumerate(data):
		print index,val,wheels[index],val ^ wheels[index]
		data[index] = val ^ wheels[index]
	print data
	if wheels[5]:
		swap(data,0,4)
	if wheels[6]:
		swap(data,0,1)
	if wheels[7]:
		swap(data,1,2)
	if wheels[8]:
		swap(data,2,3)
	if wheels[9]:
		swap(data,3,4)
	return data

def swap(data,index_1,index_2):
	temp = data[index_1]
	data[index_1] = data[index_2]
	data[index_2] = temp
	return data

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

def getCurrentWheels():
	array = []
	for wheel in wheels:
		array.append(wheel.get())
	return array

print arrayToInt([1,0,0,0,1])

msg = 'UMUM4VEVE35KING4HENRY4IV35'
print DICT[arrayToInt(encryp(getCurrentWheels(),intToArray(DICT.index('U'))))]
print DICT[arrayToInt(encryp(getCurrentWheels(),intToArray(DICT.index('M'))))]
crypt = ''
for char in msg:
	#print char
	crypt = crypt + DICT[arrayToInt(encryp(getCurrentWheels(),intToArray(DICT.index(char))))]

print crypt