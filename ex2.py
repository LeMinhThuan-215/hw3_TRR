def tenarySearch(first, last):
    while first <= last:
        #2 mid chia list thành 3 đoạn
        mid1 = first + (last-first)//3
        mid2 = first + (last-first)//3*2
        #So sánh key với giá trị tại 2 mid
        if intList[mid1] == key:
            return mid1
        if intList[mid2] == key:
            return mid2
        if key < intList[mid1]:
            last = mid1-1
        elif key < intList[mid2]:
            last = mid2-1
            first = mid1+1
        else:
            first = mid2+1
    return -1

##################################################

def printResult():
    idx = tenarySearch(0, numberOfElements-1)
    if idx == -1:
        print("Key is not exist!!")
    else:
        print("Index of key is:", idx+1)

###################################################

print("Enter number of elements:", end = ' ')
numberOfElements = int(input())

print("Enter your list:")
intList = [int(input()) for i in range(numberOfElements)]

print("Enter key you want to search:", end = ' ')
key = int(input())

printResult()