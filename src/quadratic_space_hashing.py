from src.Universal_Hashing import UniversalHashing
from src.attributes import num_of_digits


class QuadraticSpaceHashing:
    def __init__(self, size):
        self.size = int(pow(2, num_of_digits(size * size)))
        self.hash_table = [None for x in range(self.size)]
        self.hash_function = None

    # Build perfect hash table of O(n ^ 2) space
    def build_hash_table(self, keys):
        not_hashed = True
        b = num_of_digits(self.size)
        number_of_rehashing = 0
        while not_hashed:
            not_hashed = False
            number_of_rehashing += 1
            self.hash_function = UniversalHashing(b)
            self.hash_function.build_hash_function()
            for i in range(len(keys)):
                hash_value = self.hash_function.hash_value(keys[i])
                hash_value %= self.size
                if self.hash_table[hash_value] is None:
                    self.hash_table[hash_value] = keys[i]
                else:
                    self.hash_table = [None for x in range(self.size)]
                    not_hashed = True
                    break
            if number_of_rehashing > 1000:
                print("Rehashing failed")
                break

    # Find Key
    def find(self, key):
        hash_value = self.hash_function.hash_value(key)
        hash_value %= self.size
        if self.hash_table[hash_value] == key:
            return True
        else:
            return False

    def get_table(self):
        return self.hash_table
