#!/usr/bin/env python3

from math import sqrt
from math import gcd
from functools import lru_cache
import random
from random import randint
import sys
poruka = "69420"
_doDecript = True
_generate_key = False
_p = 83
_q = 89
_d = 0
_e = 17
sys.argv = sys.argv[1:]

if len(sys.argv) > 0:
    poruka = str(sys.argv[0])
    sys.argv = sys.argv[1:]

if len(sys.argv) > 0:
    if sys.argv[0] == "250":
        _p = 64135289477071580278790190170577389084825014742943447208116859632024532344630238623598752668347708737661925585694639798853367
        _q = 33372027594978156556226010605355114227940760344767554666784520987023841729210037080257448673296881877565718986258036932062711
        _e = 65537
    if sys.argv[0] == "100":
        _p = 37975227936943673922808872755445627854565536638199
        _q = 40094690950920881030683735292761468389214899724061
        _e = 65537
        # _d = 1435319569480661473883310243084583371347212233430112391255270984679722445287591616684593449660400673

    if sys.argv[0] == "6":
        _p = 845111
        _q = 923903
        _e = 65537

    if sys.argv[0] == "1":
        _p = 61
        _q = 53
        _e = 17
        # _d = 2753

@lru_cache
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    sqrtN = int(sqrt(n))+1
    for i in range(2, sqrtN):
        if n % i == 0:
            return False

    return True

def lcm(p, q):
    # for i in range(1, p*q):
    #     if (i % p == 0) and (i % q == 0):
    #         return i
    return p*q

@lru_cache
def mod_inverse(e, congurgent):
    if gcd(e, congurgent) != 1:
        print("Exponent e nije congurgentan sa ", congurgent)
        if _generate_key == True:
            print("Traženje novih faktora...")
            return -1
        else:
            exit()

    for i in range(0, e*e*e):
        if (congurgent*i+1) % e == 0:
            d = (congurgent*i+1) // e
            return d
        print(i, end="\r")
    return 0

def encrypt(msg_plaintext, public_key):
    #unpack key value pair
    e, n = public_key
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext

def decrypt(msg_ciphertext, private_key):
    d, n = private_key
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))

def generate_keypair(keysize):
    (p, q) = (0, 0)
    # keysize is the bit length of n so it must be in range(nMin,nMax+1).
    # << is bitwise operator
    # x << y is same as multiplying x by 2**y
    # i am doing this so that p and q values have similar bit-length.
    # this will generate an n value that's hard to factorize into p and q.

    fMin = 1 << (keysize - 1)
    fMax = (1 << keysize) - 1
    primes = []
    # we choose two prime numbers in range(start, stop) so that the difference of bit lengths is at most 2.
    if fMin >= fMax:
        return []
    
    for i in range(fMin - 1, fMax + 1, 2):
        if isPrime(i):
            # print(i, end="\n")
            primes.append(i)
            if len(primes) > 10000:
                i += randint(fMin, fMax)%fMin

    if len(primes) <= 2:
        print("Pre mali broj bitova za faktore!")
        exit()

    p = random.choice(primes)
    primes.remove(p)
    q = random.choice(primes)
    primes.remove(q)
    
    print(p, q)

    return (p, q)



def main():
    (p,q) = (_p, _q)

    factor_len = 0
    if _generate_key == True:
        factor_len = int(input("Enter factor bit_length: "))
        (p, q) = generate_keypair(factor_len)


    d = -1
    while d == -1:      # loop dok nije ispravan
            
        n = p*q
        ln = lcm(p - 1, q - 1)

        if _d != 0:
            d = _d
        else:
            d = mod_inverse(_e, ln)
            if d == -1:
                (p, q) = generate_keypair(factor_len)
    

    # if (poruka < 0 or poruka >= n):
    #     print("Poruka \"", poruka, "\" je pre velika za slanje!")

    print("de mod ln = ", (_e*d) % ln)
    print(" n  = ", n, "\n ln = ", ln, "\n e  = ", _e, "\n d  = ", d, "\n")

    ciphre = encrypt(poruka, (_e, n))
    print(ciphre)
    print(decrypt(ciphre, (d, n)))

    # print(int(poruka))
    # encript = pow(int(poruka), _e, n)
    # print("Encript: ", encript)
    #
    # if _doDecript:
    #     decript = pow(encript, d, n)
    #     print("Decript: ", decript)



if __name__ == "__main__":
    main()

