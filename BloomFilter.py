from bitarray import bitarray

class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len
        bit_array = bitarray(self.filter_len)
        bit_array.setall(0)


    def hash1(self, str1):
        for c int str1:
            code = ord(c)
        #реализация

    def hash2(self, str1):
        #223
        #...

    def add(self, str1):
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
