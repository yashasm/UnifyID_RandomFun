# UnifyID_RandomFun

## Repository details

This repository consists of true random number generation using Random.org API (https://www.random.org/clients/http/) and also simple RSA key generation algorithm using random generated by Random.org

## Random Number generation

RANDOM.ORG offers true random numbers to anyone on the Internet. The randomness comes from atmospheric noise, which for many purposes is better than the pseudo-random number algorithms typically used in computer programs. People use RANDOM.ORG for holding drawings, lotteries and sweepstakes, to drive online games, for scientific applications and for art and music.

### GenerateRandom.py

This file generates the true random numbers in Integer or Hex format. User can also specify the range in which he/she wants to generate the random number

example:

    print "Generated random number is: " + generateRandomNumberInInteger(100,10000) #generate single random number
    print "Generated multiple random numbers are: " + generateRandomNumbersInInteger(2) #generate 2 random numbers
    print "Generated random number in hex is: " + generateRandomNumberInHex() # generate random number in hex

    output:
    
    Generated random number is: 7927
    Generated multiple random numbers are:
    605846458
    598438231
    Generated random number in hex is: 1196ff50
    

### generateRSAKeyPair.py

This script generates the simple RSA pair using below mentioned dalgorithm

Note: For better and secure RSA key generation we should consider large prime number with 1024 digits. For simplicity I have considered the number ranging from 1 - 1000000000

1) Prime Number Generation: Two large prime numbers pp and qq need to be generated. 
2) Modulus: From the two large numbers, a modulus nn is generated by multiplying pp and qq.
3) Totient: The totient of n,ϕ(n)n,ϕ(n) is calculated.
4) Public Key: A prime number is calculated from the range [3,ϕ(n))[3,ϕ(n)) that has a greatest common divisor of 11 with ϕ(n)ϕ(n).
5) Private Key: Because the prime in step 4 has a gcd of 1 with ϕ(n)ϕ(n), we are able to determine it's inverse with respect to modϕ(n)modϕ(n).
