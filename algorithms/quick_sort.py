import random
import sys

class QuickSort():


    def __init__(self, input_dict):
        self.name = "Quick Sort"

        self.execution_time = {"best": {},
                               "worst": {},
                               "avg": {}}

        self.worst_case_inputs = input_dict['sorted']
        self.best_case_inputs = input_dict['random']
        self.avg_case_inputs = input_dict['reversed_sorted']


    def quicksort_partition(self, unsorted_list, low, high):
        partitioning_index = low - 1
        pivot = unsorted_list[high]
        for j in range(low, high):
            if unsorted_list[j] <= pivot:
                partitioning_index = partitioning_index + 1
                unsorted_list[partitioning_index], unsorted_list[j] = unsorted_list[j], unsorted_list[
                    partitioning_index]
        unsorted_list[partitioning_index + 1], unsorted_list[high] = unsorted_list[high], unsorted_list[
            partitioning_index + 1]
        return partitioning_index + 1

    def sort_algorithm(self, unsorted_list, k=None, low=None, high=None):
        if k is not None:
            k -= 1
        if low is None:
            low = 0
        if high is None:
            high = len(unsorted_list) - 1
        size = high - low + 1
        stack = [0] * size
        top = -1
        top = top + 1
        stack[top] = low
        top = top + 1
        stack[top] = high
        while top >= 0:
            high = stack[top]
            top = top - 1
            low = stack[top]
            top = top - 1
            partition_index = self.quicksort_partition(unsorted_list, low, high)
            if partition_index - 1 > low:
                top = top + 1
                stack[top] = low
                top = top + 1
                stack[top] = partition_index - 1
            if partition_index + 1 < high:
                top = top + 1
                stack[top] = partition_index + 1
                top = top + 1
                stack[top] = high
        return unsorted_list[k]
