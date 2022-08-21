def quicksort(list):
    if(len(list)<=1):
        return(list)
    else:
        pivot_element= list.pop()
        greaternumber=[]
        lowernumber=[]


    for number in list:
        if (number>pivot_element):
            greaternumber.append(number)
        else:
            lowernumber.append(number)
    return quicksort(lowernumber) + [pivot_element] + quicksort(greaternumber)







list=[6,23,8,9,11,16,15,14,7,2,1,3]
print(f'unsorted array is: {list}')
print (f'the sorted array is :{quicksort(list)}')
