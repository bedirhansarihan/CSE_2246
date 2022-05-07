import time
import random
class InsertionSort:

    def __init__(self):
        self.name = "Insertion Sort"
        self.execution_time = dict()   # key: input_size, value: execution_time

    def sort_algorithm(self, array, k):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

        return array[k]
