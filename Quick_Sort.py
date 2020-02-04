def quick_sort(array):
    if len(array)<2:
        return array
    else:
        pivot= array[0]
        less = [i for i in array[1:] if i<=pivot]
        greater = [j for j in array[1:] if j>pivot]
        return quick_sort(less)+[pivot]+ quick_sort(greater)