'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here
# Python3 program for the above approach

# Function to find the minimum number
# of moves required to sort the array
def minOperations(arr1, arr2, i, j, table):
    key = (i, j)

    # Base Cases
    if arr1 == arr2:
        return 0
    if i >= len(arr1) or j >= len(arr2):
        return 0

    # If the result is already stored
    if key in table:
        return table[key]

    # Compute the result
    if arr1[i] < arr2[j]:
        return 1 + minOperations(arr1, arr2, i + 1, j + 1, table)

    # Store the result
    table[key] = max(minOperations(arr1, arr2, i, j + 1, table), minOperations(arr1, arr2, i + 1, j, table))

    # Return the result
    return table[key]


# Function to print the minimum
# moves required to sort the array
def minOperationsUtil(arr):
    brr = sorted(arr)
    table = dict()

    # If both the arrays are equal
    if brr == arr:

        # No moves required
        print(0)

    # Otherwise
    else:
        print(len(brr) - minOperations(brr, arr, 0, 0, table))


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    # print(LIS(l))
    # print(n - LIS(l))
    minOperationsUtil(l)