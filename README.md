# RSA Encryption and Decryption

This repository contains a tutorial on how to implement RSA encryption and decryption algorithms in Python.

In order to guarantee user privacy and secure data transmission, encryption methods are used.
Information that has been encrypted is changed from plain text to a secret code that can only be accessed by the intended person.
A user of RSA creates a public key using two large prime numbers and a random integer, then makes it public. This public key for cryptography is accessible to anyone.
However, the message can only be decoded by someone who is aware of the first two numbers on which the key is founded. There is no known way to circumvent this mechanism.

This repository contains a Python implementation of the RSA encryption and decryption algorithm. RSA is a widely used asymmetric encryption algorithm that allows secure transmission of data over an insecure channel.

## How It Works

The script provides functions for generating key pairs, encrypting messages, and decrypting messages using the RSA algorithm.

- The `generate_keypair()` function generates a pair of public and private keys.
- The `encrypt(message, public_key)` function encrypts a given message using the public key.
- The `decrypt(encrypted_message, private_key)` function decrypts an encrypted message using the private key.

## Usage

1. Clone the repository to your local machine.
2. Run the script using a Python interpreter.
3. Follow the prompts to generate keys, input your message, and see the encryption and decryption process.

## Example

```python
 ... 
Public Key : (84589, 155479)
Private Key : (54229, 155479)
Write Your Msg: hello
[104, 101, 108, 108, 111]
[51200, 120688, 117788, 117788, 78690]
Encrypted msg :> 5120012068811778811778878690
Decrypted msg :> hello
