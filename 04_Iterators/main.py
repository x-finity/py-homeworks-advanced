class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        

    def __iter__(self):
        self.list = []
        # self.list = self._pop_list()
        return self
    
    def _pop_list(self):
        return self.list_of_list.pop(0)

    def __next__(self):
        try:
            if not self.list: self.list = self._pop_list()
        except IndexError:
            raise StopIteration
        item = self.list.pop(0)

        return item



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for i in range(3):
        print(list(FlatIterator(list_of_lists_1)))
    # if list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]:
    #     print(list(FlatIterator(list_of_lists_1)))
    #     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], 'Not OK!'
    #     print('OK')
    
    # for item in FlatIterator(list_of_lists_1):
    #     print(item)
    # print(list(FlatIterator(list_of_lists_1)))
    # test_1()