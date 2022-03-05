def binarySearch(key, first, last):
    while first <= last:
        #Xử lý trường hợp đặc biệt
        if  key < intList[first]:
            return first
        if key > intList[last]:
            return last+1
        #So sánh key với các giá trị quanh mid
        mid = (first+last)//2
        if intList[mid-1] <= key <= intList[mid]:
            return mid
        elif key > intList[mid]:
            first = mid+1
        else:
            last = mid

##################################################

def binaryInsertionSort():
    for i in range(1, numberOfElements):
        #Tìm vị trí thỏa mãn để chèn intList[i]
        idx = binarySearch(intList[i], 0, i-1)
        t = intList[i]
        #Dịch mảng
        for i in range(i, idx, -1):
            intList[i] = intList[i-1]
        #Chèn
        intList[idx] = t

##################################################

print("Enter number of elements:", end = ' ')
numberOfElements = int(input())

print("Enter your list:")
intList = [int(input()) for i in range(numberOfElements)]

binaryInsertionSort()

print("List after sort:", end = ' ')
for x in intList:
    print(x, end = ' ')