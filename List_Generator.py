import string
import random


class Generator:

    def __init__(self, lenght=5, size=10):
        self.length = lenght
        self.size = size

    def generate_str(self, lenght=3):
        chars = string.ascii_lowercase
        return ''.join(random.choice(chars) for _ in range(lenght))

    def generate_list(self):
        return [self.generate_str(random.randint(0, self.length)) for _ in range(self.size)]


if __name__ == '__main__':

    gen = Generator(100, 1000)
    str_list = gen.generate_list()

    print(str_list)
