def quick_sort(array):
    if len(array) < 2:
        return array            #Базовый случай - сортировка не нужна
    else:
        pivot   = array[0]        #выбираем опорный элемент
        less    = [i for i in array[1:] if i <= pivot] #Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot] #Подмассив всех элементов больше опорного

        return quick_sort(less) + [pivot] + quick_sort(greater)  #Рекурсивная сортировка каждой части массива


print(quick_sort([10,25,4,36,6,8,9,96,5,2,4]))
