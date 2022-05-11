

class PartialSelectionSort():

    def __init__(self, input_dict):
        self.name = "Partial Selection Sort"
        self.execution_time = {"best": {},
                               "worst": {},
                               "avg": {}}

        self.best_case_inputs = input_dict['sorted']
        self.worst_case_inputs = input_dict['reversed_sorted']
        self.avg_case_inputs = input_dict['random']

    def sort_algorithm(self, unsorted_list, k):
        size = len(unsorted_list)
        for i in range(k + 1):
            min_ = float("inf")
            min_index = -1
            for j in range(i, size):
                if unsorted_list[j] < min_:
                    min_index = j
                    min_ = unsorted_list[j]
            if min_index != -1:
                unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
        return unsorted_list[k]