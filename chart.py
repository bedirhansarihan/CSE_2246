import matplotlib.pyplot as plt
import typing
import pandas as pd

from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.partial_selection_sort import PartialSelectionSort
from algorithms.heap_sort import HeapSort

class Chart():


    def __init__(self, algorithms):

        self.algorithms: typing.List[QuickSort, InsertionSort, MergeSort, PartialSelectionSort, HeapSort]= algorithms

    def compare_two_algorithms(self, algo1, algo2):

        """
        Compares two algorithms according to their sorting time on each different input size

        :param algo1:
        :param algo2:
        :return:
        """

        x1_point = list(algo1.execution_time.keys())
        y1_point = list(algo1.execution_time.values())

        x2_point = list(algo2.execution_time.keys())
        y2_point = list(algo2.execution_time.values())



        fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
        ax.set_yscale('log')
        ax.plot(x1_point, y1_point, label= algo1.name)
        ax.plot(x2_point, y2_point, label= algo2.name)
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Execution Time')
        ax.set_title(f"{algo1.name} vs {algo2.name}")

        #ax = plt.gca()
        #ax.set_ylim([min(y1_point + y2_point), max(y1_point + y2_point)])
        ax.legend()
        plt.show()


    def best_worst_avg_case(self, algo: typing.Union[QuickSort, InsertionSort, MergeSort, PartialSelectionSort, HeapSort]):
        data: dict = algo.execution_time
        fig, ax = plt.subplots(figsize=(12, 6), layout='constrained')
        for case in data:
            if case == "avg":

                    x1_point = list(data[case].keys())
                    y1_point = list(data[case].values())

                    ax.plot(x1_point, y1_point, marker='o', color='black',  label="avg-case")

            if case == "best":
                    x1_point = list(data[case].keys())
                    y1_point = list(data[case].values())

                    ax.plot(x1_point, y1_point,marker='o', color='green',  label="best-case")

            if case == "worst":

                    x1_point = list(data[case].keys())
                    y1_point = list(data[case].values())

                    ax.plot(x1_point, y1_point, marker='o', color='red',  label="worst-case")

        ax.set_xlabel('Input Size')
        ax.set_ylabel('Execution Time (ms)')
        ax.set_title(algo.name)
        ax.ticklabel_format(style='plain')

        ax.legend()
        plt.show()

    def table(self, algo: typing.Union[QuickSort, InsertionSort, MergeSort, PartialSelectionSort, HeapSort]):



        fig, ax = plt.subplots(1, 1)
        data = [list(algo.execution_time['best'].values()),
                list(algo.execution_time['worst'].values()),
                list(algo.execution_time['avg'].values())]
        #column_labels = list(algo.execution_time['avg'].keys())
        column_labels = ["N=1000", "N=10000", "N=20000", "N=30000", "N=40000", "N=50000"]
        df = pd.DataFrame(data, columns=column_labels)
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=df.values, colLabels=df.columns, rowLabels=["BEST", "WORST", "AVG"], loc="center")

        plt.show()

    def compare_all_algorithms(self, algorithms: list):
        return

    def execute(self):

        for algo in self.algorithms:
            if algo.name in ["Partial Selection Sort", "Quick Sort", "Insertion Sort"]:
                continue
            self.best_worst_avg_case(algo)
            self.table(algo)
        #
        # for idx1, algo1 in enumerate(self.algorithms):
        #
        #
        #     for idx2, algo2 in enumerate(self.algorithms):
        #
        #         if idx1 >= idx2 + 1:
        #
        #             self.compare_two_algorithms(algo1, algo2)








