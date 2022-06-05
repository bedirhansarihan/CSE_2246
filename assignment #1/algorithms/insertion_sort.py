import typing



class InsertionSort():

    def __init__(self, input_dict: typing.Dict[str, typing.List[list]]):

        self.name = "Insertion Sort"

        self.execution_time = {"best": {},
                               "worst": {},
                               "avg": {}}

        self.best_case_inputs = input_dict['sorted']
        self.worst_case_inputs = input_dict['reversed_sorted']
        self.avg_case_inputs = input_dict['random']


    def sort_algorithm(self, array, k):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

        return array[k]
