import unittest

"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed 
at the correct position in the sorted part.

Characteristics of Insertion Sort:
    -This algorithm is one of the simplest algorithm with simple implementation
    -Basically, Insertion sort is efficient for small data values
    -Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.
"""


def insertion_sort(arr):
    pass


class OrdenacaoTestesSelection(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))
        

if __name__ == '__main__':
    unittest.main()
