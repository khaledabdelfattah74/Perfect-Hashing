# universal hashing class to generate hash functions and calculate the hash value of key
import random


class UniversalHashing:
    # Constructor
    def __init__(self, u, b):
        self.u = u
        self.b = b
        self.hash = [[0 for x in range(self.u)] for y in range(self.b)]

    # Generate random matrix of zeros and ones to use it in hashing process
    def build_hash_function(self):
        for i in range(self.b):
            for j in range(self.u):
                value = random.randint(0, 1)
                self.hash[i][j] = value

    # Calculate the hash value of key using the matrix method
    def hash_value(self, key):
        hash_value = 0
        for i in range(self.b):
            temp = key
            val = 0
            for j in range(self.u):
                x = self.hash[i][j] * (temp & 1)
                temp >>= 1
                val ^= x
            hash_value |= val
            hash_value <<= 1
        return hash_value
