import numpy as np



#Base Fucntion: exchage the items at position i and j
def swap(lyst,i,j):
    temp=lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp

def partition(lyst,left,right):
    #Find the pivot and exchange it with the last item
    middle=(left+right)//2
    pivot=lyst[middle]
    lyst[middle]=lyst[right]
    lyst[right]=pivot
    #Set the boundary point to first position
    boundary=left
    #Move items less than povit to the left
    for index in range(left,right):
        if lyst[index]<pivot:
            swap(lyst,index,boundary)
            boundary+=1
    #Exchange the pivot item and boundary item
    swap(lyst,right,boundary)
    return boundary


def quicksortHelper(lyst,left,right):
    if left<right:
        pivotLocation=partition(lyst,left,right)
        quicksortHelper(lyst,left,pivotLocation-1)
        quicksortHelper(lyst,pivotLocation+1,right)

def quicksort(lyst):
    quicksortHelper(lyst,0,len(lyst)-1)

def main(size):
    lyst = np.random.rand(size)
    print(lyst)
    quicksort(lyst)
    print(lyst)

if __name__=="__main__":
     main(10)

