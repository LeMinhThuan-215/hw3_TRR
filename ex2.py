def tenarySearch(key, first, last):
    mid1 = (first+last)/3
    mid2 = (first+last)/3*2
    if intList[mid1] == key:
        return mid1
    elif key < intList[mid1]:
        tenarySearch(first, mid1-1)
    elif key == mid2:
        return mid2
    elif key < intList[mid2]   


print("Enter number of list:", end=' ')
numberOfList = int(input())
print("Enter your list:")
intList = [int(input()) for i in range(numberOfList)]