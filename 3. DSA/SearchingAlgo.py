import sys
sys.stdin = open('/Users/mayank/Development/Coding Env/4. PYTHON/input.txt', 'r')
sys.stdout = open('/Users/mayank/Development/Coding Env/4. PYTHON/output.txt', 'w')

# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1,3,5,7,9,10]
target = 3
print(binary_search(arr, target))