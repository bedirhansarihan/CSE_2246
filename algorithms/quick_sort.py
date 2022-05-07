import random
import sys


class QuickSort():


    def __init__(self):

        self.name = "Quick Sort"
        self.execution_time = dict()
    def quicksort_partition(self, unsorted_list, low, high):
        partitioning_index = low - 1
        pivot = unsorted_list[high]
        for j in range(low, high):
            if unsorted_list[j] <= pivot:
                partitioning_index = partitioning_index + 1
                unsorted_list[partitioning_index], unsorted_list[j] = unsorted_list[j], unsorted_list[partitioning_index]
        unsorted_list[partitioning_index + 1], unsorted_list[high] = unsorted_list[high], unsorted_list[partitioning_index + 1]
        return partitioning_index + 1

    def sort_algorithm(self, unsorted_list, k=None, low=None, high=None):
        if low is None:
            low = 0
        if high is None:
            high = len(unsorted_list) - 1
        if len(unsorted_list) == 1:
            return unsorted_list
        if low < high:
            partitioning_index = self.quicksort_partition(unsorted_list, low, high)
            self.sort_algorithm(unsorted_list, None, low, partitioning_index - 1)
            self.sort_algorithm(unsorted_list, None, partitioning_index + 1, high)
        if k is not None:
            print("x")
            return unsorted_list[k]

