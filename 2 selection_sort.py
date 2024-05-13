# Алгоритм сортировки: Сортировка выбором

def find_smallest_index(arr):
    smallest_el = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_el:
            smallest_el = arr[i]
            smallest_index = i
    return smallest_index

def sort_arr(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest_index(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr = [5, 3, 1, 6, 8, 4, 2, 6, 8, 9, 5, 5, 1, 3, 5]
print(sort_arr(arr))