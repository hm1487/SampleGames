def encrypt(string):
	temp = ""
	for x in string:
		temp += str(ord(x)) + " "
	return temp

def decrypt(string):
	temp = ""
	translate = ''
	counter = 0
	holder = 0
	while (True):
		while (string[holder] != " " and holder != len(string)-1):
			holder += 1
		translate = int(string[counter:holder])
		temp += chr(translate)
		if (holder == len(string)-1):
			break
		else:
			holder += 1
			counter = holder
	return temp


def main():
	string = str(input("Input a string to be encrypted: "))
	enc = encrypt(string)
	print(enc)
	dec = decrypt(enc)
	print(dec)


main()
