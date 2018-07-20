def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low + high) // 2
        guess = list[mid]
        #这个相等的判断不可以放在else里，因为如果这个数值不存在的话会出现判断错误
        if guess == item:
            return mid

        if guess < item:
            low = mid + 1

        else:
            high = mid - 1
    #若退出循环仍没有找到，则返回None
    return None

list = [1,3,5]
print(binary_search(list,3))

