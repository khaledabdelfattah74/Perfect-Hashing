import math
from src.file_reader import read_from_file
from src.linear_space_hashing import LinearSpaceHashing
from src.quadratic_space_hashing import QuadraticSpaceHashing


def main():
    keys = read_from_file("/Users/khaledabdelfattah/PycharmProjects/PerfectHashing/src/dictionary.txt")

    # Linear space solution
    linear_hashing = LinearSpaceHashing(len(keys))
    linear_hashing.build_hash_table(keys)
    print(linear_hashing.get_table())

    # Quadratic space solution
    quadratic_hashing = QuadraticSpaceHashing(len(keys))
    quadratic_hashing.build_hash_table(keys)
    print(quadratic_hashing.get_table())


main()
