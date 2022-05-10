# Python program to generate Worst Case of Merge Sort
import random
# Function to join left and right subarray
import typing


def join(arr, left, right, l, m, r):
    i = 0
    for i in range(m - l + 1):
        arr[i] = left[i]
        i += 1

    for j in range(r - m):
        arr[i + j] = right[j]


# Function to store alternate elements in left
# and right subarray
def split(arr, left, right, l, m, r):
    for i in range(m - l + 1):
        left[i] = arr[i * 2]

    for i in range(r - m):
        right[i] = arr[i * 2 + 1]


# Function to generate Worst Case of Merge Sort
def permutated_input(arr, l, r):
    if (l < r):
        m = l + (r - l) // 2

        # create two auxiliary arrays
        left = [0 for i in range(m - l + 1)]
        right = [0 for i in range(r - m)]

        # Store alternate array elements in left
        # and right subarray
        split(arr, left, right, l, m, r)

        # Recurse first and second halves
        permutated_input(left, l, m)
        permutated_input(right, m + 1, r)

        # join left and right subarray
        join(arr, left, right, l, m, r)


def random_input(input_size: list) -> typing.List[list]:
    data = []
    for i in range(len(input_size)):
        data.append(random.sample(range(1, 500000),input_size[i]))


    return data

def sorted_input(lists: typing.List[list]) -> typing.List[list]:
    data = []

    for l in lists:
        data.append(sorted(l))

    return data

def reversed_sorted_input(sorted_lists: typing.List[list]) -> typing.List[list]:
    data = []

    for l in sorted_lists:
        data.append(list(reversed(l)))

    return data

def same_input(lists: typing.List[list]) -> typing.List[list]:
    data = []

    for l in lists:
        data.append([0 for i in range(len(l))])

    return data



# driver program
if __name__ == '__main__':
    # sorted array
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(arr)
    print("Sorted array is")
    print(arr)

    # generate Worst Case of Merge Sort
    permutation_input(arr, 0, n - 1)

    print("\nInput array that will result in \n" + "worst case of merge sort is ")

    print(arr)

    # This code contributed by shikhasingrajput
