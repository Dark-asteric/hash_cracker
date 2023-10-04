import hashlib
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet("Hash Cracker : ")
print(ascii_banner)

print("Algorithms are available: MD5 | SHA1 | SHA224 | SHA512 | SHAH384")

hash_type = str(input("Enter Your hash type : "))
wordlist_location = str(input("Enter wordlist location : "))
hash = str(input("Enter your hash : "))

word_list = open(f"{wordlist_location}").read()
lists = word_list.splitlines()

for word in lists:
    if hash_type == 'MD5':
        hash_object = hashlib.md5(f'{word}'.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1:32m Hash found: {word} \n")
    elif hash_type == 'SHA1':
        hash_object = hashlib.sha1(f'{word}'.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1:32m Hahs found: {word} \n")
    elif hash_type == 'SHA224':
        hash_object = hashlib.sha224(f'{word}'.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1:32m Hash found. {word} \n")
    elif hash_type == 'SHA512':
        hash_object = hashlib.sha512(f'{word}'.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033 [1:32m Hash found. {word} \n")
    elif hash_type == 'SHA384':
        hash_object = hashlib.sha384(f'{word}'.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f'\033[1:32m Hash found. {word} \n')
    else:
        print("Your choosen hash_type is not valid. Try again !!!")

