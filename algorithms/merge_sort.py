import time
import random
import typing

class MergeSort():

    def __init__(self, input_dict):

        self.name = "Merge Sort"
        self.execution_time = {"best": {},
                               "worst": {},
                               "avg": {}}


        self.best_case_inputs = input_dict['sorted']
        self.worst_case_inputs = input_dict['permutated']
        self.avg_case_inputs = input_dict['random']




    def sort_algorithm(self, array, k=0):

        if len(array) > 1:

            #  r is the point where the array is divided into two subarrays
            r = len(array) // 2
            L = array[:r]
            M = array[r:]

            # Sort the two halves
            self.sort_algorithm(L)
            self.sort_algorithm(M)

            i = j = y = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[y] = L[i]
                    i += 1
                else:
                    array[y] = M[j]
                    j += 1
                y += 1


            while i < len(L):
                array[y] = L[i]
                i += 1
                y += 1

            while j < len(M):
                array[y] = M[j]
                j += 1
                y += 1

            return array[k]

