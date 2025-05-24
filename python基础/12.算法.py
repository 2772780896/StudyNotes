# 选择排序
a = [2,12,9,7]
def selectSort(list):
    copyList = []
    for i in list:
        copyList.append(i)
    sortedList = []
    for i in range(list.__len__()):
        index = 0
        while index < (copyList.__len__()):
            if index == 0:
                max = copyList[index]
                maxIndex = index
            else:
                if copyList[index] > max:
                    max = copyList[index]
                    maxIndex = index
            index += 1
        print(max)
        copyList.pop(maxIndex)
        sortedList.append(max)
    return sortedList

print(selectSort(a))