
import numpy as np

#Base Fucntion: exchage the items at position i and j
def swap(lyst,i,j):
    temp=lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp

#1 Selection Sort Fucntion
def selectionSort(lyst):
    for i in range(len(lyst)-1):
        minIndex=i
        j=i+1
        while j <len(lyst):
            if lyst[j]<lyst[minIndex]:
                minIndex=j
            j+=1
        if minIndex!=i:
            swap(lyst,minIndex,i)
        i+=1

#2 Bubble Sort Function
def bubbleSort(lyst):
    n=len(lyst)
    while n >1:
        for i in range(n-1):
            if lyst[i+1]<lyst[i]:
                swap(lyst,i,i+1)
        n-=1


#3 Insert Sort Function
def insertionSort(lyst):
    i=1
    while i<len(lyst):
        itemToInsert=lyst[i]
        j=i-1
        while j>=0:
            if itemToInsert<lyst[j]:
                lyst[j+1]=lyst[j]
                j -= 1
            else:
                break
        lyst[j+1]=itemToInsert
        i+=1


def main(size):
    lyst = np.random.rand(size)
    print(lyst)
    # selectionSort(lyst)
    # bubbleSort(lyst)
    insertionSort(lyst)
    print(lyst)

if __name__=="__main__":
     main(10)


