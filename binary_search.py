#Реализация бинарного поиска
def binary_search(list, item):
    low     = 0             #В этих переменных храним границы той части списка,
    high    = len(list)-1   #в которой выполняется поиска

    while low <= high:              #Пока не останется одна позиция
        mid = (low+high)            #Проверяем средний элемент
        guess = list[mid]
        if guess == item:           #Если искомое значение равно середине
            return mid              #возвращаем ничего
        if guess > item:            #Если много
            high = mid-1
        else:                       #Если мало
            low = mid+1

    return None                     #Если значение не существует

my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3)  # =>1
print binary_search(my_list, -1)  # =>None
