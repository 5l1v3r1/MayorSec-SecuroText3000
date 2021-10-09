import pyperclip
import os
import time


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.!:"=+][@#$%^&*?-_></\)( \n'
def banner():
    print("-" * 60)
    print("               MayorSec Vigenere Cipher Tool            ")
    print("                       Version 1.0.0                    ")
    print("                   A project by The Mayor               ")
    print("-" * 60)
    time.sleep(1)
    #This section collects the message you want to encrypt/decrypt, accept your key input, and encrypt or decrypt based on your choice
    print("This tool accepts file names that you want encrypted or decrypted.")
    print("Decryption will require the correct key to be successful.")
    time.sleep(1)

def encrypt():
    print("-" * 60)
    global myMessage
    global myKey
    myMessage = input("Enter the .txt file you want encrypted or decrypted: ")
    myKey = input("Please enter your key phrase: ")

def main():
    print("\nWould you like to encrypt or decrypt your file?")
    print("-" * 60)
    print("1 = Encrypt")
    print("2 = Decrypt")
    time.sleep(.5)
    myMode = input("please enter your selection: ")
    if myMode == '1':
        fo = open(myMessage)
        content = fo.read()
        translated = encryptMessage(myKey, content)
        file = open("encrypted." + myMessage, "w")
        file.write(translated)
        file.close
    elif myMode == '2':
        fo = open(myMessage)
        content = fo.read()
        translated = decryptMessage(myKey, content)
        file = open("decrypted." + myMessage, "w")
        file.write(translated)
        file.close
    else:
        print("[-] Improper Selection.  Please make a valid selection.")
        main()
	
    print('You selected option number %s. Your message is:' % (myMode.title()))
    print(translated)
	
def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')
	
def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')
	
	
def translateMessage(key, message, mode):
    translated = [] # Stores the encrypted/decrypted message string
	
    keyIndex = 0
    key = key.upper()
	
    for symbol in message: #Loops through each symbol in the message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not located in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # Add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # Subtracts if decrypting
				
            num %= len(LETTERS) # Manages wraparound
            translated.append(LETTERS[num])

            keyIndex += 1 # Moves to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
                
    return ''.join(translated)
	
if __name__ == '__main__':
    banner()
    encrypt()
    main()