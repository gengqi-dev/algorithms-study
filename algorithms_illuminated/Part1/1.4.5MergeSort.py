def MergeSort(arr: list):
    if len(arr) <= 1:
        return arr
    else:
        m = len(arr) // 2
        highArray = MergeSort(arr[:m])
        lowerArray = MergeSort(arr[m:])
        res = []
        i = 0
        j = 0
        while i < len(highArray) and j < len(lowerArray):
            print(highArray)
            print(lowerArray)
            if highArray[i] < lowerArray[j]:
                res.append(highArray[i])
                i += 1
            else:
                res.append(lowerArray[j])
                j += 1
        if i < len(highArray):
            res.extend(highArray[i:])
        else:
            res.extend(lowerArray[j:])
        return res


print(MergeSort([3, 1, 2, 34, 123, 12]))
