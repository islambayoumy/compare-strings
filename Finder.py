from collections import Counter

class Finder:

    def __init__(self, str_list):
        self.str_list = str_list

    def compare_str(self, str1, str2):
        if len(str1) != len(str2):
            return False  # O(1)

        return Counter(str1) == Counter(str2)  # O(n)
