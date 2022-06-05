

class QuickSelectV1():

    # pivot always first element
    def __init__(self, input_dict):
        self.name = "Quick Select v1"
        self.execution_time = {"best": {},
                               "worst": {},
                               "avg": {}}

        self.worst_case_inputs = input_dict['sorted']
        self.best_case_inputs = input_dict['random']
        self.avg_case_inputs = input_dict['reversed_sorted']

    def sort_algorithm(self,unsorted_list, k, low=None, high=None):
        if low is None:
            low = 0
        if high is None:
            high = len(unsorted_list) - 1
        while True:
            value = unsorted_list[high]
            index = low
            for j in range(low, high):
                if unsorted_list[j] <= value:
                    unsorted_list[index], unsorted_list[j] = unsorted_list[j], unsorted_list[index]
                    index += 1
            unsorted_list[index], unsorted_list[high] = unsorted_list[high], unsorted_list[index]
            if index - low == k - 1:
                return unsorted_list[index]
            if index - low > k - 1:
                high = index - 1
                continue
            k = k - index + low - 1
            low = index + 1



