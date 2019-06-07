from collections import Counter
from List_Generator import Generator


class Finder:

    def __init__(self, str_list):
        self.str_list = str_list

    def compare_str(self, str1, str2):
        if len(str1) != len(str2):
            return False  # O(1)

        return Counter(str1) == Counter(str2)  # O(n)

    def find(self, string):
        # O(n^2)
        return [s for s in self.str_list if self.compare_str(string, s)]


def test_fun():  # pragma: no cover
    gen = Generator(5, 50)
    str_list = gen.generate_list()

    finder = Finder(str_list)
    result = finder.find(str_list[10])

    return result


if __name__ == '__main__':  # pragma: no cover
    print(test_fun())
