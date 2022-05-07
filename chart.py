import matplotlib.pyplot as plt
import typing


from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort

class Chart():


    def __init__(self, algorithms):

        self.algorithms: typing.List[InsertionSort, MergeSort]= algorithms

    def compare_two_algorithms(self, algo1, algo2):

        x1_point = list(algo1.execution_time.keys())
        y1_point = list(algo1.execution_time.values())

        x2_point = list(algo2.execution_time.keys())
        y2_point = list(algo2.execution_time.values())



        fig, ax = plt.subplots(figsize=(15, 10), layout='constrained')
        ax.plot(x1_point, y1_point, label= algo1.name)
        ax.plot(x2_point, y2_point, label= algo2.name)
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Execution Time')
        ax.set_title(f"{algo1.name} vs {algo2.name}")

        #ax = plt.gca()
        #ax.set_ylim([min(y1_point + y2_point), max(y1_point + y2_point)])
        ax.legend()
        plt.show()
    def execute(self):

        for idx1, algo1 in enumerate(self.algorithms):


            for idx2, algo2 in enumerate(self.algorithms):

                if idx1 >= idx2 + 1:

                    self.compare_two_algorithms(algo1, algo2)








