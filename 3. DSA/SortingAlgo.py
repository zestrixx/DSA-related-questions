import sys
sys.stdin = open('/Users/mayank/Development/Coding Env/4. PYTHON/input.txt', 'r')
sys.stdout = open('/Users/mayank/Development/Coding Env/4. PYTHON/output.txt', 'w')


a = list(map(int, input().split()))

# $$$$$$$$$$$$$$$$$$$$$$$$ selection sort $$$$$$$$$$$$$$$$$$$$$$$$

"""
Time Complexity: O(n^2)
"""


def selection_sort(a):
    for i in range(len(a)-1):
        minIdx = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIdx]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]

    print("selection sort :", a)

# $$$$$$$$$$$$$$$$$$$$$$$$ Bubble sort $$$$$$$$$$$$$$$$$$$$$$$$


"""
Worst Case Time Complexity: O(n^2) when arr is reverse sorted
Best Case Time Complexity : O(n) when arr is already sorted
"""


def bubble_sort(a):
    for i in range(len(a)):
        swapped = False
        for j in range(len(a)-i-1):  # 5-0-1, 5-1-1, 5-2-1, 5-3-1, 5-4-1
            ''' in every loop the largest element is pushed to the last
                for i==0
                64 25 12 22 11
                25 64 12 22 11 ->1st
                25 12 64 22 11 ->2nd
                25 12 22 64 11 ->3rd
                25 12 22 11 64 ->4th

                again the same process happens till i==4
            '''
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        # if no swap happened in inner loop means array is already sorted, so no need to run the loop for O(n^2) times.
        if swapped == False:
            break
    print("bubble sort :", a)


# $$$$$$$$$$$$$$$$$$$$$$$$ Insertion Sort $$$$$$$$$$$$$$$$$$$$$$$$

"""
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

Time Complexity: O(n^2)
"""


def insertion_sort(a):
    for i in range(1, len(a)):
        # taking current ele to compare to all its predecessor(before) elements.
        curr = a[i]
        prev = i-1
        while prev >= 0 and a[prev] > curr:
            a[prev+1] = a[prev]  # moving greater ele one step right
            prev -= 1
        # here we'll assign the curr(smaller) ele at right position after moving all greater ele to right.
        a[prev+1] = curr
    print("insertion sort :", a)


# $$$$$$$$$$$$$$$$$$$$$$$$ Merge Sort $$$$$$$$$$$$$$$$$$$$$$$$

"""
Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

Time Complexity : θ(n*logn)
"""


def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]

        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
            
        # Checking if any element was left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
 
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


selection_sort(a)
bubble_sort(a)
insertion_sort(a)
merge_sort(a)
print('merge sort : ', a)
