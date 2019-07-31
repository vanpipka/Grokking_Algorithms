def findSmallest(array):
    smallest = array[0]             #Для хранения наименьшего значения
    smallest_index = 0              #Для хранения индекса наименьшего значения
    for i in range(0, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index

def selectionSort(array):           #Функция сортировки массива
    newArray = []
    for i in range(0, len(array)):
        smallest = findSmallest(array)          #Находим индекс наименьшего
        newArray.append(array.pop(smallest))    #Удааляем его из исходного массива и добавляем в результат

    return newArray

print(selectionSort([5,3,6,2,10]))
