import hashlib

flag = 0

pass_hash = input("Enter md5 hash:")

wordlist = input("Enter File Name:")

try:
	pass_file = open ( wordlist, "r")
except:
	print("No File Found")
	quit()

for word in pass_file:

	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()


	print(word)
	print(digest)
	print(pass_hash)

	if digest == pass_hash:
		print("Password Found:")
		print("Password Is: " +  word)
		flag = 1
		break

if flag == 0:
	print("Password/Passphase Is Not In List")

 
