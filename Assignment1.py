import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], " ")
    print()

def randomize(size):
    arr=[]
    for i in range(size):
        arr.append(random.randint(0, size * 10))
    return arr

if __name__ == '__main__':
    size = int(sys.argv[1])
    sizeB = int(sys.argv[2])
    sizeC = int(sys.argv[3])

    print("\nInsertion sort:")
    f = plt.figure(1)
    times = []
    elements = 1
    arr = randomize(size)
    for i in range(size):
        start = time.time_ns()
        insertionSort(arr)
        end = time.time_ns()
        times.append(end-start)
        elements+=1
        arr = randomize(elements)
    print(times)
    x = np.linspace(0,elements, size)
    plt.plot(x, times, label="Insertion Sort")



    print("\nMerge Sort:")
    times = []
    elements = 1
    arr = randomize(size)
    for i in range(size):
        start = time.time_ns()
        mergeSort(arr)
        end = time.time_ns()
        times.append(end-start)
        elements+=1
        arr = randomize(elements)
    print(times)
    x = np.linspace(0,elements, size)
    plt.plot(x, times, label="Merge Sort")
    f.show()
    plt.legend()
    plt.xlabel('Elements in Array', fontsize=12)
    plt.ylabel('Runtime of Algorithm in ns', fontsize=12)
    plt.suptitle('Insertion vs Merge Sort', fontsize=18)



    print("\nInsertion sort:")
    g = plt.figure(2)
    times = []
    elements = 1
    arr = randomize(size)
    for i in range(sizeB):
        start = time.time_ns()
        insertionSort(arr)
        end = time.time_ns()
        times.append(end-start)
        elements+=1
        arr = randomize(elements)
    print(times)
    x = np.linspace(0,elements, sizeB)
    plt.plot(x, times, label="Insertion Sort")

    print("\nMerge Sort:")
    times = []
    elements = 10
    arr = randomize(size)
    for i in range(sizeB):
        start = time.time_ns()
        mergeSort(arr)
        end = time.time_ns()
        times.append(end-start)
        elements+=1
        arr = randomize(elements)
    print(times)
    x = np.linspace(0,elements, sizeB)
    plt.plot(x, times, label="Merge Sort")
    g.show()
    plt.legend()
    plt.xlabel('Elements in Array', fontsize=12)
    plt.ylabel('Runtime of Algorithm in ns', fontsize=12)
    plt.suptitle('Insertion vs Merge Sort', fontsize=18)



    print("\nInsertion sort:")
    h = plt.figure(3)
    times = []
    elements = 1
    arr = randomize(size)
    for i in range(sizeC):
        start = time.time_ns()
        insertionSort(arr)
        end = time.time_ns()
        times.append(end-start)
        elements+=1
        arr = randomize(elements)
    print(times)
    x = np.linspace(0,elements, sizeC)
    plt.plot(x, times, label="Insertion Sort")

    print("\nMerge Sort:")
    times = []
    elements = 10
    arr = randomize(size)
    for i in range(sizeC):
        start = time.time_ns()
        mergeSort(arr)
        end = time.time_ns()
        times.append(end-start)
        elements+=1
        arr = randomize(elements)
    print(times)
    x = np.linspace(0,elements, sizeC)
    plt.plot(x, times, label="Merge Sort")
    h.show()
    plt.legend()
    plt.xlabel('Elements in Array', fontsize=12)
    plt.ylabel('Runtime of Algorithm in ns', fontsize=12)
    plt.suptitle('Insertion vs Merge Sort', fontsize=18)
    plt.show()