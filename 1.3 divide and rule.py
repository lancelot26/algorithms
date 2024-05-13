# Разделяй и властвуй: Рекурсия

def sum(arr):
    if len(arr) == 1:
        return arr
    else:
        x = arr[0]
        arr.pop(0)
        return x + sum(arr)