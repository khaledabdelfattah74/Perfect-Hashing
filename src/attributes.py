import math


# Simple function to read keys from a file
def read_from_file(path):
    try:
        file = open(path, "r")
        line = file.read()
        if line[len(line) - 1] == ',':
            line = line[:len(line) - 1] + line[(len(line)):]
        keys_set = set(line.split(","))
        keys = [0] * len(keys_set)
        print(len(keys_set))
        i = 0
        for key in keys_set:
            keys[i] = int(key)
            i += 1
        file.close()
        return keys
    except IOError as exception:
        raise exception


def num_of_digits(num):
    digits = math.log(num, 2)
    if int(digits) == math.ceil(digits):
        digits += 1
    return int(math.ceil(digits))
