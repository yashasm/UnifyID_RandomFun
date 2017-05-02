import requests

def generateRandomNumberInInteger(min = -1000000000, max = 1000000000):
    '''
     generate single random number in integer with given range
    '''
    param = {"num": 1, "min": min, "max": max, "col": 1, "base": 10, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return response.content

def generateRandomNumbersInInteger(num, min = -1000000000, max = 1000000000):
    '''
    generate random numbers in integer with given range
    '''
    param = {"num": num, "min": min, "max": max, "col": 1, "base": 10, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return response.content

def generatePositiveRandomInteger(max = 1000000000):
    '''
    generate single random positive number in integer with given range
    '''
    param = {"num": 1, "min": 1, "max": max, "col": 1, "base": 10, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return response.content

def generateRandomNumbersInInteger(num,max = 1000000000):
    '''
    generate random positive numbers in integer with given range
    '''
    param = {"num": num, "min": 1, "max": max, "col": 1, "base": 10, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return response.content

def generateRandomNumberInHex(min = -1000000000, max = 1000000000):
    '''
    generate single random number in hex with given range
    '''
    param = {"num": 1, "min": min, "max": max, "col": 1, "base": 16, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return response.content

def generateRandomNumbersInHex(num,min = -1000000000, max = 1000000000):
    '''
        generate random numbers in hex with given range
    '''
    param = {"num": num, "min": min, "max": max, "col": 1, "base": 16, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return response.content

if __name__ == "__main__":
    print "Generated random number is: " + generateRandomNumberInInteger()
    print "Generated multiple random numbers are: " + generateRandomNumbersInInteger(10)
    print "Generated random number in hex is: " + generateRandomNumberInHex()
