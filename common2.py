__author__ = 'Jac'
import random

def generateRandomString(ran, length):
    result = ""
    ranUnic = ran.decode("utf8")
    while len(result) < length:
        value = ranUnic[random.randint(0, len(ranUnic)-1)]
        if result.find(value) is -1:
            result += value
        elif len(result) >= len(ranUnic):
            result += value
    return result.encode("utf8")