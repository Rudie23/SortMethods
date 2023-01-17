import unittest

"""The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending 
order) from the unsorted part and putting it at the beginning.

The algorithm maintains two subarrays in a given array.

    -The subarray which already sorted. 
    -The remaining subarray was unsorted.

The subarray which already sorted. The remaining subarray was unsorted. In every iteration of the selection sort, 
the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the beginning of 
unsorted subarray.

After every iteration sorted subarray size increase by one and unsorted subarray size decrease by one."""


def selection_sort(arr):
    ordered_array = list()
    for _ in list(arr):
        minimum_value = min(arr)
        ordered_array.append(minimum_value)
        arr.remove(minimum_value)
    return ordered_array


class OrdenacaoTestesSelection(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], selection_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], selection_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], selection_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], selection_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
