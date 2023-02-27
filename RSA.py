import random
from random import randint

def isprime(n):
    # تشخیص عدد اول
    if n <= 1:
        return False
    elif n <= 3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

# ============================================================================= #

def gcd(a, b):
    # محاسبه ب.م.م از طریق الگوریتم اقلیدوسی
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
# ============================================================================= #

def mod_inverse(a, m):
    # محاسبه وارون ضربی پیمانه ای
    # باقیمانده‌ی حاصلضرب e*d به n = 1
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# دو عدد تصادفی انتخاب میکنیم
p = randint(1, 1000)
q = randint(1, 1000)

# ============================================================================= #

def generate_keypair(p, q):
    # keysize : طول کلید
    # x << y برابر است با x * 2**y

    primes = []
    for i in range(1, 1000, 1):
        if isprime(i) == True:
            primes.append(i)

    # از بین اعداد اول تولید شده دو عدد تصادفی انتخاب میکنیم
    while primes != []:
        p = random.choice(primes)
        primes.remove(p)  # p != q
        q = random.choice(primes)
        break
    print(f"p:{p} , q:{q}")
    n = p * q
    t = (p - 1) * (q - 1)
    # φ(n) = lcm (p-1 ,q-1) = |(p-1)*(q-1)| / gcd(p-1,q-1)

    while True:
        #  1 < e < phi(n) and gcd(e,phi) = 1
        # اگه ب.م.م دو عدد یک باشه میگیم این دو عدد نسبت به هم اولند 
        e = random.randrange(1, t)
        g = gcd(e, t)
        # d*e ≡ 1 (mod n)
        d = mod_inverse(e, t)
        if g == 1 and e != d:
            break

    # public key = (e , n)
    # private key = (d , n)
    # e ~ encryption
    # d ~ decryption

    return ((e, n), (d, n))

# ============================================================================= #

def encrypt(Massage, package):
    # c = m^e  mod n
    # pow(base, exp, mod) -> base^exp % mod
    e, n = package
    msg_secrettext = [pow(ord(x), e, n) for x in Massage]
    return msg_secrettext

# ============================================================================= #

def decrypt(msg_secrettext, package):
    # m = c^d  mod n
    d, n = package
    Massage = [chr(pow(x, d, n)) for x in msg_secrettext]
    return (''.join(Massage))

# ============================================================================= #

print(" ... ")
public, private = generate_keypair(p, q)
print(f"Public Key : {public}")
print(f"Private Key : {private}")
msg = input("Write Your Msg: ")
print([ord(i) for i in msg])
encrypted_msg = encrypt(msg, public)
print(encrypted_msg)
print(f"Encrypted msg :> {''.join(map(lambda x: str(x), encrypted_msg))} ")
print(f"Decrypted msg :> {decrypt(encrypted_msg, private)} ")