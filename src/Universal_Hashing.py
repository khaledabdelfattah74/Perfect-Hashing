# universal hashing class to generate hash functions and calculate the hash value of key
import random


class UniversalHashing:
    __u = 32

    # Constructor
    def __init__(self, b):
        self.__b = b
        self.hash = [[0 for x in range(self.__u)] for y in range(self.__b)]

    # Generate random matrix of zeros and ones to use it in hashing process
    def build_hash_function(self):
        for i in range(self.__b):
            for j in range(self.__u):
                value = random.random()
                self.hash[i][j] = True if (round(value) == 1) else False

    # Calculate the hash value of key using the matrix method
    def hash_value(self, key):
        hash_value = 0
        for i in range(self.__b):
            temp = key
            val = 0
            for j in range(self.__u):
                flag = True if (temp & 1) else False
                x = self.hash[i][j] & flag
                temp >>= 1
                val ^= x
            hash_value |= val
            hash_value <<= 1
        return hash_value
