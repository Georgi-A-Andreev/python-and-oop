class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self) -> None:
        self.x = IntegerList(1, 2, 3, 's')

    def test_constructor(self):
        self.assertEqual(self.x._IntegerList__data, [1, 2, 3])

    def test_get_data(self):
        self.assertEqual(self.x.get_data(), [1, 2, 3])

    def test_add(self):
        self.assertEqual(self.x.add(4), [1, 2, 3, 4])
        with self.assertRaises(ValueError) as case:
            self.x.add('S')
        self.assertEqual(str(case.exception), "Element is not Integer")

    def test_remove_index(self):
        self.assertEqual(self.x.remove_index(0), 1)
        with self.assertRaises(IndexError) as case:
            self.x.remove_index(10)
        self.assertEqual(str(case.exception), "Index is out of range")

    def test_init(self):
        self.assertEqual(self.x.get_data(), [1, 2, 3])

    def test_get(self):
        self.assertEqual(self.x.get(0), 1)
        with self.assertRaises(IndexError) as case:
            self.x.get(10)
        self.assertEqual(str(case.exception), "Index is out of range")

    def test_insert(self):
        with self.assertRaises(IndexError) as case:
            self.x.insert(10, 4)
        self.assertEqual(str(case.exception), "Index is out of range")

        with self.assertRaises(ValueError) as case:
            self.x.insert(1, 'S')
        self.assertEqual(str(case.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.x.get_biggest(), 3)

    def test_get_index(self):
        self.assertEqual(self.x.get_index(2), 1)


if __name__ == '__main__':
    unittest.main()
