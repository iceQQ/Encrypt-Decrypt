from __future__ import print_function
from acropolis import *
import string
import sys


def encrypt():
    def in_put(text):
    	if (sys.version_info.major >= 3):
		import base64 
		inp = input(str(text))
		return inp
	else:
		inp = raw_input(str(text))
		return inp
    def decryption():
	print("Enter text")
	text = in_put("> ")
	print("\n")
	en = {"b":"a", "c":"b", "d":"c", "e":"d", "f":"e", "g":"f", "h":"g", "i":"h", "j":"i", "k":"j", "l":"k", "m":"l", "n":"m", "o":"n", "p":"o", "q":"p", "r":"q", "s":"r", "t":"s", "u":"t", "v":"u", "w":"v", "x":"w", "y":"x", "z":"y", "0":"z", "9":"1", "8":"2", "7":"3", "6":"4", "5":"6", "4":"6", "3":"7", "2":"8", "1":"9", " ":" " }
	for letter in text:
    		print(en[letter], end='')
	print("\n")
    def encryption():
	print("Enter text")
	text = in_put("> ")
	print("\n")
	en = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h", "h":"i", "i":"j", "j":"k", "k":"l", "l":"m", "m":"n", "n":"o", "o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v", "v":"w", "w":"x", "x":"y", "y":"z", "z":"0", "1":"9", "2":"8", "3":"7", "4":"6", "5":"4", "6":"5", "7":"3", "8":"2", "9":"1", " ":" " }
	for letter in text:
    		print(en[letter], end='')
	print("\n")
	exit()
    def banner():
        print("	1. Encrypt")
        print("	2. Decrupt")
	print("	3. Exit")
	opt = in_put("> ")
	if opt == "1":
		encryption()
	elif opt == "2":
		decryption()
	else:
		exit()
    banner()

encrypt()






