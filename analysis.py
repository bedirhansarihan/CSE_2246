import typing
import random
from chart import Chart

from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.partial_selection_sort import PartialSelectionSort
from algorithms.heap_sort import HeapSort

import time
class Analysis:

    def __init__(self, algorithms: list):



        self.insertion_sort = algorithms[0]             # 1
        self.merge_sort = algorithms[1]                 # 2
        self.quick_sort = algorithms[2]                 # 3
        self.partial_selection_sort = algorithms[2]     # 4
        self.heap_sort = algorithms[3]                  # 5
        # self.quick_select1 = algorithms[5]              # 6
        # self.quick_select2 = algorithms[6]              # 7
        self.algorithm_list = [self.insertion_sort, self.merge_sort, self.partial_selection_sort, self.heap_sort]
        self.chart = Chart(self.algorithm_list)

        self.inputs: dict = self.create_valid_inputs()
        self.k: list = self.create_valid_k()


        self.execute()
        self.chart.execute()

    def create_valid_inputs(self) -> typing.Dict[int, typing.List[int]]:
        input_dict = {}
        input_size = 500


        for i in range(4):
            input_dict[input_size] = random.sample(range(1, 500000), input_size)
            input_size *= 2

        return input_dict

    def create_valid_k(self) -> typing.List[int]:
        random_k_list = []

        for input_size in self.inputs.keys():
            random_k_list.append(random.randint(0, input_size))

        return random_k_list




    def analyze_algorithms(self, algo: typing.Union[InsertionSort, MergeSort, QuickSort, PartialSelectionSort, HeapSort]):

        list_dict: dict = self.inputs
        for i, (input_size, list) in enumerate(list_dict.items()):

            start_time = time.time()

            print(algo.sort_algorithm(list, self.k[i])
                  )

            algo.execution_time[input_size] = time.time() - start_time


    def execute(self):
        #calculates the execution time with different input_size for each algorithms
        for algo in self.algorithm_list:

            self.analyze_algorithms(algo)





