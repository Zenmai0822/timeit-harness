import timeit

test_functions = ["one", "two", "three"]

STMT = """
from harness import main
main.{}()
"""

if __name__ == "__main__":
    for test_function in test_functions:
        print("Running {}".format(test_function))
        print(timeit.timeit(STMT.format(test_function)))
        print("----------")