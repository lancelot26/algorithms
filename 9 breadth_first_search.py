from collections import deque

# Поиск в ширину: Графы

def search_name(name):
    search_queue = deque()   # Создаём очередь
    search_queue += graph[name]   # Загружаем в очередь первое рукопожатие
    searched = []   # Список проверенных
    while search_queue:
        person = search_queue.popleft()   # Выгружаем первый элемент
        if not person in searched:   # проверка на повтор проверенных
            if person == 'michael':
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

graph = {}
graph["you"] = ["alex", "tony", "mike"]   #Первое рукопожатие

graph["alex"] = ["michael", "kirill"]   #Второе рукопожатие
graph["tony"] = ["bob"]
graph["mike"] = ["bob"]

graph["kirill"] = ["bob"]     #Третье рукопожатие
graph["michael"] = []
graph["bob"] = []

print(search_name("you"))