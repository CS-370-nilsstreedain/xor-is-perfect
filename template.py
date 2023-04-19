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

secret_array = []

# write your code to get the plaintext of the secret numbers and on
def xor_decrypt(data, key):
	return [chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(data, key)]

# Extract the key by XORing plaintext with ciphertext
key = xor_decrypt(byte_plaintext, byte_ciphertext)

print(p.readline().strip())

# Decrypt the secret number using the extracted key and send to process
p.sendline(''.join(xor_decrypt(byte_secret_number, key)).encode('hex'))

for _ in range(5): print(p.readline().strip())

# Decrypt/print flag
print(''.join(xor_decrypt(p.readline().strip().decode('hex'), key)))
