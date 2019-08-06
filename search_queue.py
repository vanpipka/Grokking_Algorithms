from collections import deque

graph = {}
graph["you"]    = [ "alice", "bob", "claire"]
graph["bob"]    = ["anuj", "peggy"]
graph["alice"]  = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"]   = []
graph["peggy"]  = []
graph["thom"]   = []
graph["jonny"]  = []

def person_is_seller(name):
    return name[-1] == 'm'

def search_queque(persons):
    while persons:
        person = persons.popleft()
        if person_is_seller(person):
            print(person + " is а mango seller ! ")
            return True
        else:
            persons += graph[person]

    return False

search_queue = deque()
search_queue += graph ["you"]

search_queque(search_queue)
