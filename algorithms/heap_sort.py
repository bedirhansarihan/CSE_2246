


class HeapSort():


    def __init__(self):

        self.name = "Heap Sort"
        self.execution_time = dict()

    def heapify(self, unsorted_list, size, index):
        largest = index
        index1 = 2 * index + 1
        index2 = 2 * index + 2
        if index1 < size and unsorted_list[largest] < unsorted_list[index1]:
            largest = index1
        if index2 < size and unsorted_list[largest] < unsorted_list[index2]:
            largest = index2
        if largest != index:
            unsorted_list[index], unsorted_list[largest] = unsorted_list[largest], unsorted_list[index]
            self.heapify(unsorted_list, size, largest)

    def sort_algorithm(self, unsorted_list, k):
        size = len(unsorted_list)
        for index in range(size // 2 - 1, -1, -1):
            self.heapify(unsorted_list, size, index)
        for index in range(size - 1, k, -1):
            unsorted_list[index], unsorted_list[0] = unsorted_list[0], unsorted_list[index]
            self.heapify(unsorted_list, index, 0)
        return unsorted_list[0]
