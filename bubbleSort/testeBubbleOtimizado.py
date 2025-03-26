import time
from bubbleOtimizado import bubble_sort_otimizado

lista = [11, 4, 30, 22, 7, 26]

print("Lista desordenada: ", lista)

inicio = time.time()
bubble_sort_otimizado(lista)
fim = time.time()

print("Lista ordenada: ", lista)

print(f"Tempo gasto: {fim - inicio:.6f} segundos", flush=True)