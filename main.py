

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

multi_list = [
    'a',
    ['1', '2', '3'],
    [[5, 7, 8, 9], 'b', 'c', ['11', '12', '13', '14'], 5],
    100, 102, 103,
    [200, 202, 208],
    ['x', [300, 400, 500, 600, 700], [800, 900], 'y'],
]


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.nested_list):
            while (self.j < len(self.nested_list[self.i])):
                self.j += 1
                return self.nested_list[self.i][self.j - 1]
            self.i += 1
            self.j = 0
        raise StopIteration


class FlatIteratorPro:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.extra_queue = []
        self.curr_iter = iter(self.multi_list)
        return self

    def __next__(self):
        while True:
            try:
                self.curr_item = next(self.curr_iter)
            except StopIteration:
                if not self.extra_queue:
                    raise StopIteration
                else:
                    self.curr_iter = self.extra_queue.pop()
                    continue
            if isinstance(self.curr_item, list):
                self.extra_queue.append(self.curr_iter)
                self.curr_iter = iter(self.curr_item)
            else:
                return self.curr_item


def flat_gen(nested_list):
    for sub_list in nested_list:
        for item in sub_list:
            yield item


def flat_gen_pro(some_list):
    for item in some_list:
        if not isinstance(item, list):
            yield item
        else:
            yield from flat_gen_pro(item)


if __name__ == '__main__':

    print('Flat iterator:')
    for item in FlatIterator(nested_list):
        print(item)
    print('-------------------------\n')

    print('Comperhension iterator:')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('-------------------------\n')

    print('Flat generator:')
    for item in flat_gen(nested_list):
        print(item)
    print('-------------------------\n')

    print('Flat iterator pro: ')
    for item in FlatIteratorPro(multi_list):
        print(item)
    print('-------------------------\n')

    print('Comperhansion iterator pro:')
    flat_list_pro = [item for item in FlatIteratorPro(multi_list)]
    print(flat_list_pro)
    print('-------------------------\n')

    print('Flat generator pro:')
    for item in flat_gen_pro(multi_list):
        print(item)
    print('-------------------------\n')
