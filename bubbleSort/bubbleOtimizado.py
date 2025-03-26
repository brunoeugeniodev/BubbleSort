def bubble_sort_otimizado(array):
    n = len(array)
    for i in range(n - 1):
        swapped = False  # Flag para verificar se houve troca
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:  # Se nenhuma troca foi feita, o array já está ordenado
            break
