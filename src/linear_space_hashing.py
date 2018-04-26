from src.Universal_Hashing import UniversalHashing
from src.quadratic_space_hashing import QuadraticSpaceHashing
from src.attributes import num_of_digits


class LinearSpaceHashing:
    __number_of_rehashing = 0

    def __init__(self, size):
        self.__size = int(pow(2, num_of_digits(size)))
        self.__hash_table = [[] for x in range(self.__size)]
        self.__hash_function = None
        self.__hash_functions = [QuadraticSpaceHashing for x in range(self.__size)]

    # Build perfect hash table of O(n ^ 2) space
    def build_hash_table(self, keys):
        b = num_of_digits(self.__size)
        self.__hash_function = UniversalHashing(b)
        self.__hash_function.build_hash_function()
        for i in range(len(keys)):
            hash_value = self.__hash_function.hash_value(keys[i])
            hash_value %= self.__size
            # print(hash_value)
            self.__hash_table[hash_value].append(keys[i])
        for i in range(self.__size):
            if len(self.__hash_table[i]) == 0:
                continue
            quadratic_hashing = QuadraticSpaceHashing(len(self.__hash_table[i]))
            quadratic_hashing.build_hash_table(self.__hash_table[i])
            self.__hash_table[i] = quadratic_hashing.get_table()
            self.__hash_functions[i] = quadratic_hashing
            self.__number_of_rehashing += quadratic_hashing.get_number_of_rehashing()

    def find(self, key):
        hash_value = (self.__hash_function.hash_value(key)) % self.__size
        return self.__hash_functions[hash_value].find(key)

    def get_table(self):
        return self.__hash_table

    def get_number_of_rehashing(self):
        return self.__number_of_rehashing
