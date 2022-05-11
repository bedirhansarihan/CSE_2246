import typing

from chart import Chart

from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.partial_selection_sort import PartialSelectionSort
from algorithms.heap_sort import HeapSort
from algorithms.quick_select import QuickSelectV1

from generate_input import *
import time
class Analysis:

    def __init__(self,):

        self.inputs: typing.Dict[str, typing.List[list]] = self.create_random_inputs([1000, 10000,20000,30000,40000,50000])
        self.k= self.create_random_k()

        self.quick_sort = QuickSort(self.inputs)
        self.insertion_sort = InsertionSort(self.inputs)
        self.merge_sort = MergeSort(self.inputs)
        self.partial_selection_sort = PartialSelectionSort(self.inputs)
        self.heap_sort = HeapSort(self.inputs)
        self.quick_select_v1 = QuickSelectV1(self.inputs)

        self.algorithm_list = [self.quick_sort, self.insertion_sort, self.merge_sort,  self.partial_selection_sort, self.heap_sort, self.quick_select_v1]

        self.chart = Chart(self.algorithm_list)
        self.execute()
        self.chart.execute()

    def create_random_inputs(self, list_size: list) -> typing.Dict[str, typing.List[list]]:
        """
        In order to test algorithm efficiency, it creates different lists with different sizes.
        :return:
        """
        input_dict = {}

        input_dict['random'] = random_input(list_size)
        input_dict['sorted'] = sorted_input(input_dict['random'])
        input_dict['reversed_sorted'] = reversed_sorted_input(input_dict['sorted'])
        input_dict['same'] = same_input(input_dict['random'])

        data = []
        for list in input_dict['sorted']:
            x = list.copy()
            permutated_input(x, 0, len(x) -1)
            data.append(x)

        input_dict['permutated'] = data

        return input_dict


    def create_random_k(self) -> typing.List[int]:
        """
        Generates a random k values for each N size random generated array.
        :return:
        """
        random_k_list = []

        for input_size in list(self.inputs.values())[0]:
            random_k_list.append(random.randint(0, len(input_size)-1))

        return random_k_list


    def analyze_algorithms(self, algo: typing.Union[QuickSort, InsertionSort, MergeSort,  PartialSelectionSort, HeapSort, QuickSelectV1]):
        """
        Calculates the execution time with different input size for each algorithms

        :param algo:
        :return:
        """
        for i, l in enumerate(list(self.inputs.values())[0]):
        # avg_case
            input_size = len(l)
            start_time = time.time() * 1000

            algo.sort_algorithm(algo.avg_case_inputs[i], self.k[i])
            algo.execution_time["avg"][input_size] = round(time.time() * 1000 - start_time, 4)
            print(f"avg_case for {algo.name} algortihms:->> {algo.execution_time['avg'][input_size]}")

        # best_case

            start_time = time.time() * 1000
            if algo.name == "Partial Selection Sort":
                algo.sort_algorithm(algo.best_case_inputs[i], 1)
                algo.execution_time['best'][input_size] = round(time.time() * 1000 - start_time, 4)
                print(f"best_case for {algo.name} algortihms:->> {algo.execution_time['best'][input_size]}")
            else:

                algo.sort_algorithm(algo.best_case_inputs[i], self.k[i])
                algo.execution_time['best'][input_size] =round(time.time() * 1000 - start_time, 4)
                print(f"best_case for {algo.name} algortihms:->> {algo.execution_time['best'][input_size]}")

        # worst_case

            start_time = time.time() * 1000
            if algo.name == "Partial Selection Sort":
                algo.sort_algorithm(algo.worst_case_inputs[i], len(algo.worst_case_inputs[i])-1)
                algo.execution_time['worst'][input_size] = round(time.time() * 1000 - start_time, 4)
                print(f"worst_case for {algo.name} algortihms:->> {algo.execution_time['worst'][input_size]}")
                print(f'FOR N IS {input_size}\n')
            else:
                algo.sort_algorithm(algo.worst_case_inputs[i], self.k[i])
                algo.execution_time['worst'][input_size] = round(time.time() * 1000 - start_time, 4)
                print(f"worst_case for {algo.name} algortihms:->> {algo.execution_time['worst'][input_size]}")
                print(f'FOR N IS {input_size}\n')
    def execute(self):
        print('start')
        start_exec_time = time.time()
        for algo in self.algorithm_list:
            if algo.name in ["Quick Select v1"]:

                self.analyze_algorithms(algo)


        total_exec_time = time.time() -start_exec_time
        print(total_exec_time)





