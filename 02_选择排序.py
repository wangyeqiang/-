def select_sort(list):
    n = len(list)
    for i in range(n):
        #min = list[i]
        for j in range(i+1,n):
            if list[j] < list[i]:
                # list[i] = list[j]
                # list[j] = min
                list[i],list[j] = list[j],list[i]
    return list
list = [1,3,5,7,2,4,5,4,2,5,9,7,8,1,23,3,4,6,7,8,6,8,9,7,1,2,3,8,4,56,456,12,1]
print(select_sort(list))