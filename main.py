from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.partial_selection_sort import PartialSelectionSort
from algorithms.heap_sort import HeapSort
import sys
from analysis import Analysis

if __name__ == '__main__':
    # instances of algorithms
    sys.setrecursionlimit(9999)

    merge_srt = MergeSort()
    insertion_srt = InsertionSort()
    quick_srt = QuickSort()
    partial_selection_srt = PartialSelectionSort()
    heap_srt = HeapSort()
    algorithms = [insertion_srt, merge_srt, quick_srt, partial_selection_srt, heap_srt]

    # analysis part
    analysis = Analysis(algorithms)



