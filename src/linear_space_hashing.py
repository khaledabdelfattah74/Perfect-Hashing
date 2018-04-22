from src.Universal_Hashing import UniversalHashing
from src.quadratic_space_hashing import QuadraticSpaceHashing
from src.attributes import num_of_digits


class LinearSpaceHashing:
    def __init__(self, size):
        self.size = int(pow(2, num_of_digits(size)))
        self.hash_table = [[] for x in range(self.size)]
        self.hash_function = None
        self.hash_functions = [QuadraticSpaceHashing for x in range(self.size)]

    # Build perfect hash table of O(n ^ 2) space
    def build_hash_table(self, keys):
        b = num_of_digits(self.size)
        self.hash_function = UniversalHashing(b)
        self.hash_function.build_hash_function()
        for i in range(len(keys)):
            hash_value = self.hash_function.hash_value(keys[i])
            hash_value %= self.size
            self.hash_table[hash_value].append(keys[i])
        for i in range(self.size):
            if len(self.hash_table[i]) == 0:
                continue
            quadratic_hashing = QuadraticSpaceHashing(len(self.hash_table[i]))
            quadratic_hashing.build_hash_table(self.hash_table[i])
            self.hash_table[i] = quadratic_hashing.get_table()
            self.hash_functions[i] = quadratic_hashing

    def find(self, key):
        hash_value = (self.hash_function.hash_value(key)) % self.size
        return self.hash_functions[hash_value].find(key)

    def get_table(self):
        return self.hash_table
