import sys

ORDA 			= ord('a')		#Order of 'a' character
ORDZ			= ord('z')		#Order of 'z' character
ALPHALENGTH		= 26			#Alphabet length

def vigenere(key, string, encrypt):
	encryptedString	= ''			#Encrypted string
	offset			= 0				#Offset key for non alpha characters

	#Encrypt
	for i in range(len(string)):
		capitalized = string[i].isupper()

		#Get character order
		stringOrd 	= ord(string[i].lower())

		#Get key character as if it were looped and get order
		keyOrd		= ord(key[(i-offset)%len(key)])

		if stringOrd not in range(ORDA, ORDZ+1):
			#Character is not alpha
			encryptedString += string[i]
			offset += 1
		else:
			if encrypt:
				newOrd = vigenereEncrypt(stringOrd, keyOrd)
			else:
				newOrd = vigenereDecrypt(stringOrd, keyOrd)
			
			#Add to string
			if capitalized:
				encryptedString += chr(newOrd).upper()
			else:
				encryptedString += chr(newOrd)

	return encryptedString

def vigenereEncrypt(cOrd, kOrd):
	#Compute encrypted character order
	order = cOrd + kOrd - ORDA

	#If new order is greater than z's order, loop back to beginning of alphabet
	if order > ORDZ:
		order -= ALPHALENGTH

	return order

def vigenereDecrypt(cOrd, kOrd):
	#Compute encrypted character order
	order = cOrd - kOrd + ORDA

	#If new order is less than a's order, loop it back in range
	if order < ORDA:
		order += ALPHALENGTH

	return order

def main(args):
	if len(args) > 3:
		key 		= args[1]
		string 		= args[2]
		doEncrypt 	= (args[3] == 'True')

		print(vigenere(key, string, doEncrypt))
	else:
		print('Incorrect arguments. Usage: vigenere.py key string encrypt(True/False)')

if __name__ == "__main__":
    main(sys.argv)