import math


# Simple function to read keys from a file
def read_from_file(path):
    try:
        file = open(path, "r")
        keys = file.readlines()
        for i in range(len(keys)):
            keys[i] = int(keys[i])
        file.close()
        return keys
    except IOError as exception:
        raise exception


def num_of_digits(num):
    digits = math.log(num, 2)
    if int(digits) == math.ceil(digits):
        digits += 1
    return int(math.ceil(digits))
