#!/usr/bin/env python

from pwn import *

p = process("./xor-is-perfect")

# get some intro lines
print(p.readline().strip())
print(p.readline().strip())
print(p.readline().strip())
print(p.readline().strip())
print(p.readline().strip())

# get plaintext
plaintext = p.readline().strip()
print('plaintext: %s' % plaintext)

# get some useless lines
print(p.readline().strip())
print(p.readline().strip())

# get ciphertext
ciphertext = p.readline().strip()
print('ciphertext: %s' % ciphertext)
# get newline
print(p.readline().strip())

# decode plain and the ciphertext from hexcode to byte
byte_plaintext = plaintext.decode('hex')
byte_ciphertext = ciphertext.decode('hex')

# print each of them
print(byte_plaintext)
print(byte_ciphertext)

# we will store the key as integers
key = []

print(p.readline().strip())

# get the secret number
secret_number = p.readline().strip()
print('secret_number: %s' % secret_number)
# get the byte of the secret number
byte_secret_number = secret_number.decode('hex')

plain_secret_array = []

# write your code to get the plaintext of the secret numbers and on
# Extract the key by XORing plaintext with ciphertext
for (text_c, key_c) in zip(byte_plaintext, byte_ciphertext):
	key.append(chr(ord(text_c) ^ ord(key_c)))

# Decrypt the secret number using the extracted key
for (text_c, key_c) in zip(byte_secret_number, key):
	plain_secret_array.append(chr(ord(text_c) ^ ord(key_c)))

print(p.readline().strip())
p.sendline(''.join(plain_secret_array).encode('hex'))

print(p.readline().strip())
print(p.readline().strip())
print(p.readline().strip())
print(p.readline().strip())
print(p.readline().strip())

bytes_flag = p.readline().strip().decode('hex')

plain_flag = []

for (text_c, key_c) in zip(bytes_flag, key):
        plain_flag.append(chr(ord(text_c) ^ ord(key_c)))

print(''.join(plain_flag))
