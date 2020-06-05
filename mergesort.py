# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        idx_left_arr = idx_right_arr = idx_merged_arr = 0

        # Copy data to temp arrays L[] and R[]
        while idx_left_arr < len(L) and idx_right_arr < len(R):
            if L[idx_left_arr] < R[idx_right_arr]:
                arr[idx_merged_arr] = L[idx_left_arr]
                idx_left_arr += 1
            else:
                arr[idx_merged_arr] = R[idx_right_arr]
                idx_right_arr += 1
            idx_merged_arr += 1

        # Checking if any element was left
        while idx_left_arr < len(L):
            arr[idx_merged_arr] = L[idx_left_arr]
            idx_left_arr += 1
            idx_merged_arr += 1

        while idx_right_arr < len(R):
            arr[idx_merged_arr] = R[idx_right_arr]
            idx_right_arr += 1
            idx_merged_arr += 1

# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

# This code is contributed by Mayank Khanna
