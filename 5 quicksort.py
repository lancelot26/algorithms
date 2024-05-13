# Алгоритм быстрой сортировки: Разделяй и властвуй: Рекурсия

def quick_sort(arr):
    if len(arr) < 2:    # Базовый случай, условие завершения
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)

arr = [5, 6, 2, 6, 53 ,1, 4, 7, 1, 4, 15]
print(quick_sort(arr))