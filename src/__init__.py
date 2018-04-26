import sys

from src.attributes import read_from_file
from src.linear_space_hashing import LinearSpaceHashing
from src.quadratic_space_hashing import QuadraticSpaceHashing


def main():
    try:
        keys = read_from_file("../src/testCases_lab4/keys100001000000.txt")
        # Linear space solution
        linear_hashing = LinearSpaceHashing(len(keys))
        linear_hashing.build_hash_table(keys)
        # print(linear_hashing.get_table())
        print("linear", linear_hashing.get_number_of_rehashing())

        # Quadratic space solution
        quadratic_hashing = QuadraticSpaceHashing(len(keys))
        quadratic_hashing.build_hash_table(keys)
        # print(quadratic_hashing.get_table())
        print("Quadratic", quadratic_hashing.get_number_of_rehashing())
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    sys.exit(0)


if __name__ == "__main__":
    main()
