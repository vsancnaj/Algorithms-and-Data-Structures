import datetime
import csv
import pandas as pd
from matplotlib import pyplot as plt


# create randomized array
def random_array(size=200, max=550):
    from random import randint
    return [randint(0, max) for _ in range(size)]


# Insertion Sort
def insertionSort(A, first, last):
    # Traverse through array
    first += 1
    for first in range(1, last):

        key = A[first]

        # Insert A[first] into the sorted sequence A[1.. first -1]
        i = first - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


# Merge Sort
def merge_Sort(A, first, last, k):
    if first < last:
        # The k-length has been reached
        if (last - first) <= k:
            insertionSort(A, first, last)
            # print("Insertion Sort")
        # Recursive use of merge sort
        else:
            mid = (first + last) // 2
            # print("Merge Sort")
            # sort the first half
            merge_Sort(A, first, mid, k)
            # sort the second half
            merge_Sort(A, mid + 1, last, k)
            # merge
            merge(A, mid)


def merge(A, mid):
    # n1 = mid - first + 1
    # n2 = last - mid
    # Divide the array elements
    L = A[:mid]
    R = A[mid:]
    x = y = 0
    z = first

    # Copy data to temp array L and R
    while x < len(L) and y < len(R):
        if L[x] < R[y]:
            A[z] = L[x]
            x += 1
        else:
            A[z] = R[y]
            y += 1
        z += 1

    # remaining values no yet placed in A
    while x < len(L):
        A[z] = L[x]
        x += 1
        z += 1
    while y < len(R):
        A[z] = R[y]
        y += 1
        z += 1


####################### M    A   I   N #######################

with open("output.csv", "w", newline="") as f:
    # Setting up csv file
    fieldnames = ["K_value", "Best_Case", "Average_Case", "Worst_Case"]
    theWriter = csv.DictWriter(f, fieldnames=fieldnames)
    theWriter.writeheader()

    #  Function parameters
    A = random_array()
    first = 0
    last = len(A)

    # Print original
    print("Input Array:")
    print(A)

    for k in range(0, len(A),2):
        print("K-value:")
        print(k)
        # Best case
        best_arr = A
        insertionSort(best_arr, first, last)
        best_start = datetime.datetime.now()
        merge_Sort(best_arr, first, last, k)
        best_end = datetime.datetime.now()
        best_time_elapsed = best_end - best_start

        print("Best Case:")
        print(best_time_elapsed.microseconds)
        print(best_arr)

        # Average case
        average_arr = A
        average_start = datetime.datetime.now()
        merge_Sort(average_arr, first, last, k)
        average_end = datetime.datetime.now()
        average_elapsed_time = average_end - average_start

        print("Average case:")
        print(average_elapsed_time.microseconds)
        print(average_arr)

        # Worst case
        worst_arr = best_arr
        worst_arr.reverse()
        worst_start = datetime.datetime.now()
        merge_Sort(worst_arr, first, last, k)
        worst_end = datetime.datetime.now()
        worst_time_elapsed = worst_end - worst_start

        print("Worst case:")
        print(worst_time_elapsed.microseconds)
        print(worst_arr)

        # Write k, best, average, and worst into file

        best_micro = best_time_elapsed.microseconds
        average_micro = average_elapsed_time.microseconds
        worst_micro = worst_time_elapsed.microseconds
        # make dictionary
        theWriter.writerow(
            {"K_value": k, "Best_Case": best_micro, "Average_Case": average_micro, "Worst_Case": worst_micro})

# Retrieve CSV file to plot
output_data = pd.read_csv("output.csv")
plt.plot(output_data.K_value, output_data.Best_Case*10)
plt.plot(output_data.K_value, output_data.Average_Case*10)
plt.plot(output_data.K_value, output_data.Worst_Case*10)
# Labels
plt.title("Problem 2.1(b)")
plt.xlabel("K values")
plt.ylabel("Computation time (ms)")
plt.legend(["Best Case", "Average Case", "Worst Case"])
plt.show()
