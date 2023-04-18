# (In-)secure XOR Practice
Now it's time to break XOR.

XOR offers the perfect security, but we talked in the class that (if we use it in-securely) an adversary can break it.

Please proceed to the `xor-is-perfect` folder. You will find the following files after the ls command:
```
flag template.py xor-is-perfect
```

Please fix the `template.py` file. This file runs `xor-is-perfect` file, which
1. Gives you the ciphertext and plaintexts
2. Gives you another secret number (a secret message)
3. Wait for the plaintext message of the secret message

You are required to extract the key and decrypt the secret number you will get from the step 2. All this procedure is managed by `template.py`. Your job is to edit the file so that finally you can return the correct plaintext to `xor-is-perfect` file. Once you're successful, you will get the flag
