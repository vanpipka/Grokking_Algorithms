graph = {}         #Граф переходов со стоимостью каждого ребра
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}


costs = {}          #Таблица стоимостей
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float('inf')

parents = {}        #Таблица родителей
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

processed = []      #Таблица обработаных узлов

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:                                     #Перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:   #Если узел имеет наименьшую стоимость и не был ранее обработан
            lowest_cost = cost                             #То он назначаеся новым узлом с наименьшей стоимостью 
            lowest_cost_node = node

    print(node, ':', lowest_cost)
    return lowest_cost_node

node = find_lowest_cost_node(costs)         #Ищем узел с наименьшей стоимостью среди необработанных

while node != None:                         #Если обработаны все узлы, то цикл завершится
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():              #Перебор всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:             #Если к соседу можно быстрее добраться через текущий узел, то
            costs[n] = new_cost             #обновляем стоимость узла
            parents[n] = node               #Этот узел становится новым родителем для соседа

    processed.append(node)                  #Помечаем узел как обработанный
    node = find_lowest_cost_node(costs)     #Ищем следующий узел для обработки и повторяем цикл

print(costs)
