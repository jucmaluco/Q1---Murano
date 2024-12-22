import random
import time
from matplotlib import pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    return result

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    #recursão
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

# for N = 10^3
def time_comparison(sizes, num_trials):
    times = {"Bubble Sort": [], "Quick Sort": [], "Merge Sort": []}

    for size in sizes:
        bs_time, qs_time, ms_time = 0, 0, 0  # Acumula tempos para trials

        random_array = [random.randint(-100000, 100000) for _ in range(size)]

        # Bubble Sort
        arr_copy = random_array[:]
        start = time.time()
        bubble_sort(arr_copy)
        bs_time += time.time() - start

        # Quick Sort
        arr_copy = random_array[:]
        start = time.time()
        quick_sort(arr_copy)
        qs_time += time.time() - start

        # Merge Sort
        arr_copy = random_array[:]
        start = time.time()
        merge_sort(arr_copy)
        ms_time += time.time() - start

        # Calcula o tempo médio para cada algoritmo
        times["Bubble Sort"].append(bs_time / num_trials)
        times["Quick Sort"].append(qs_time / num_trials)
        times["Merge Sort"].append(ms_time / num_trials)
        print("Quick Sort:")
        print(qs_time)
        print("Bubble Sort:")
        print(bs_time)
        print("Merge Sort")
        print(ms_time)
    return times

# Plotando os resultados
sizes = [10, 200, 400, 800, 1000]  # Diferentes tamanhos de array
num_trials = 1
times = time_comparison(sizes, num_trials)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(sizes, times["Bubble Sort"], label="Bubble Sort")
plt.plot(sizes, times["Quick Sort"], label="Quick Sort")
plt.plot(sizes, times["Merge Sort"], label="Merge Sort")
plt.xlabel("Tamanho do Array")
plt.ylabel("Tempo de Execução (s)")
plt.title("Comparação de Algoritmos de Ordenação")
plt.legend()
plt.grid(True)
plt.show()


