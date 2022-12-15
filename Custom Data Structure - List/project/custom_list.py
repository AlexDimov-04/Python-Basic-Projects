from functools import reduce


class CustomList:
    def __init__(self, *args):
        self.items = [*args]

    def __result_list(self):
        return tuple(self.items)

    def __list_range_validation(self, idx):
        if not -len(self.items) <= idx < len(self.items):
            raise Exception('Index beyond list boundary!')

    def __list_value_validation(self, value):
        if value not in self.items:
            raise Exception('The given value does not contain in the list!')

    def append(self, value):
        self.items += [value]
        return self.__result_list()

    def remove(self, index):
        self.__list_range_validation(index)

        unnecessary_value = self.items[index]
        self.items = tuple([x for x in self.items if x != self.items[index]])
        return unnecessary_value

    def get(self, index):
        self.__list_range_validation(index)
        return self.items[index]

    def extend(self, iterable):
        try:
            self.items += iterable
            return self.__result_list()
        except TypeError:
            raise Exception('The parameter is not iterable!')

    def insert(self, index, value):
        if not -len(self.items) <= index < len(self.items) + 1:
            raise Exception('Index beyond list boundary!')

        self.items = self.items[:index] + [value] + self.items[index:]
        return self.__result_list()

    def pop(self):
        if not len(self.items):
            raise Exception('List length cannot be empty!')

        self.items = self.items[:len(self.items) - 1]
        return self.__result_list()

    def clear(self):
        self.items = []

    def index(self, value):
        self.__list_value_validation(value)
        return [idx for idx, el in enumerate(self.items) if el == value][0]

    def count(self, value):
        self.__list_value_validation(value)

        count = 0
        for el in self.items:
            if el == value:
                count += 1

        return count

    def reverse(self):
        self.items = self.items[::-1]
        return self.__result_list()

    def copy(self):
        return list(self.items)

    def size(self):
        return len(self.items)

    def add_first(self, value):
        self.items = [value] + self.items
        return self.__result_list()

    def dictionize(self):
        dct = {}
        try:
            for idx in range(0, len(self.items), 2):
                dct[self.items[idx]] = self.items[idx + 1]
        except IndexError:
            dct[self.items[-1]] = None

        return dct

    def move(self, amount):
        return tuple(self.items[amount:] + self.items[:amount])

    def sum(self):
        total = 0
        for el in self.items:
            if isinstance(el, int):
                total += el
            else:
                total += len(el)

        return total

    def overbound(self):
        biggest_value = max([n for n in self.items if type(n) == int])

        for el in [x for x in self.items if type(x) != int]:
            if len(el) > biggest_value:
                biggest_value = el

        return self.items.index(biggest_value)

    def underbound(self):
        smallest_value = min([n for n in self.items if type(n) == int])

        for el in [x for x in self.items if type(x) != int]:
            if len(el) < smallest_value:
                smallest_value = el

        return self.items.index(smallest_value)

    def even_only(self):
        result = []

        for el in self.items:
            if isinstance(el, int):
                if el % 2 == 0:
                    result.append(el)
            else:
                if len(el) % 2 == 0:
                    result.append(el)

        return tuple(result)

    def odd_only(self):
        result = []

        for el in self.items:
            if isinstance(el, int):
                if el % 2 != 0:
                    result.append(el)
            else:
                if len(el) % 2 != 0:
                    result.append(el)

        return tuple(result)

    def prime_only(self):
        result = []

        for el in self.items:
            if isinstance(el, int):
                if el > 1:
                    for i in range(2, el):
                        if el % i == 0:
                            break
                    else:
                        result.append(el)
            else:
                for i in range(2, len(el)):
                    if len(el) % i == 0:
                        break

                else:
                    result.append(el)

        return tuple(result)

    def descend(self):
        return tuple(sorted(self.items, key=lambda x: -x))

    def unique(self):
        return tuple({num for num in self.items})

    def operate(self, operation):
        if operation == '+':
            return reduce(lambda x, y: x + y, self.items)
        elif operation == '-':
            return reduce(lambda x, y: x - y, self.items)
        elif operation == '/':
            return reduce(lambda x, y: x / y, self.items)
        elif operation == '*':
            return reduce(lambda x, y: x * y, self.items)
