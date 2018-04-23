from src.Universal_Hashing import UniversalHashing
from src.attributes import num_of_digits


class QuadraticSpaceHashing:
    def __init__(self, size):
        self.__size = int(pow(2, num_of_digits(size * size)))
        self.__hash_table = [None for x in range(self.__size)]
        self.__hash_function = None

    # Build perfect hash table of O(n ^ 2) space
    def build_hash_table(self, keys):
        not_hashed = True
        b = num_of_digits(self.__size)
        number_of_rehashing = 0
        while not_hashed:
            not_hashed = False
            number_of_rehashing += 1
            self.__hash_function = UniversalHashing(b)
            self.__hash_function.build_hash_function()
            for i in range(len(keys)):
                hash_value = self.__hash_function.hash_value(keys[i])
                hash_value %= self.__size
                if self.__hash_table[hash_value] is None:
                    self.__hash_table[hash_value] = keys[i]
                else:
                    self.__hash_table = [None for x in range(self.__size)]
                    not_hashed = True
                    break
            if number_of_rehashing > 1000:
                print("Rehashing failed")
                break

    # Find Key
    def find(self, key):
        hash_value = self.__hash_function.hash_value(key)
        hash_value %= self.__size
        if self.__hash_table[hash_value] == key:
            return True
        else:
            return False

    def get_table(self):
        return self.__hash_table
