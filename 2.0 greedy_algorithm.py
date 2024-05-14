# Жадный алгоритм - оптимальный алгоритм (не идеальный, но и не медленный)
# С каждой итерацией откусываем как можно больший кусок искомого,
# пока соберём не всё, что нужно или пока не закончатся итерации

states_needed = {'mt','wa','or','id','nv','ut','ca','az'}   # Нужные станции
#states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# Юзаем множество, если станции могут повторятся. В остальном - всё аналогично

stations = {   # Радиостанциями, которые будем откусывать, собирая станции
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'ns', 'ut'},
    'kfive': {'ca', 'az'},
}

final_stations = set()   # Список кусков, которые в итоге собрали

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # Пересечение множеств
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            final_stations.add(best_station)
            states_needed -= states_covered

print(final_stations)