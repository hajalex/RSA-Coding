import random

def isprime(n):
    """
    Checks if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# ============================================================================= #

def gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The GCD of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# ============================================================================= #

def mod_inverse(a, m):
    """
    Calculates the modular multiplicative inverse of a number a mod m.

    Args:
        a: The number.
        m: The modulus.

    Returns:
        The modular inverse of a modulo m, or -1 if no inverse exists.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# ============================================================================= #

def generate_keypair():
    """
    Generates a pair of public and private keys for RSA encryption.

    Returns:
        A tuple containing the public key and the private key.
    """
    primes = [i for i in range(1, 1000) if isprime(i)]
    p = random.choice(primes)
    primes.remove(p)
    q = random.choice(primes)
    n = p * q
    t = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(1, t)
        g = gcd(e, t)
        d = mod_inverse(e, t)
        if g == 1 and e != d:
            break
            
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# ============================================================================= #

def encrypt(message, public_key):
    """
    Encrypts a message using RSA encryption.

    Args:
        message: The message to be encrypted.
        public_key: The public key (e, n).

    Returns:
        A list of encrypted values representing the encrypted message.
    """
    e, n = public_key
    encrypted_message = [pow(ord(x), e, n) for x in message]
    return encrypted_message

# ============================================================================= #

def decrypt(encrypted_message, private_key):
    """
    Decrypts an encrypted message using RSA decryption.

    Args:
        encrypted_message: The encrypted message.
        private_key: The private key (d, n).

    Returns:
        The decrypted message as a string.
    """
    d, n = private_key
    decrypted_message = [chr(pow(x, d, n)) for x in encrypted_message]
    return ''.join(decrypted_message)

# ============================================================================= #

print(" ... ")
public, private = generate_keypair()
print(f"Public Key : {public}")
print(f"Private Key : {private}")
message = input("Write Your Msg: ")
print([ord(i) for i in message])
encrypted_message = encrypt(message, public)
print(encrypted_message)
encrypted_message_str = ''.join(map(lambda x: str(x), encrypted_message))
print(f"Encrypted msg :> {encrypted_message_str} ")
print(f"Decrypted msg :> {decrypt(encrypted_message, private)} ")
