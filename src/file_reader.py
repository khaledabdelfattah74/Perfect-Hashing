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


def find_largest_num(keys):
    max_num = 0
    for i in keys:
        max_num = max(max_num, i)
    return num_of_digits(max_num)


def num_of_digits(num):
    return math.ceil(math.log(num, 2))
