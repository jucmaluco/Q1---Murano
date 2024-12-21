import random
import time

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
    """
    Combina duas listas ordenadas em uma única lista ordenada.
    :param left: Lista ordenada à esquerda.
    :param right: Lista ordenada à direita.
    :return: Lista combinada e ordenada.
    """
    # Lista para armazenar o resultado da fusão.
    result = []
    left_index, right_index = 0, 0  # Índices para percorrer as listas esquerda e direita.

    # Passo 1: Comparar os elementos das duas listas e adicionar o menor ao resultado.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])  # Adiciona o menor elemento da esquerda.
            left_index += 1  # Avança para o próximo elemento na esquerda.
        else:
            result.append(right[right_index])  # Adiciona o menor elemento da direita.
            right_index += 1  # Avança para o próximo elemento na direita.

    # Passo 2: Adicionar os elementos restantes (se houver) da lista esquerda.
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Passo 3: Adicionar os elementos restantes (se houver) da lista direita.
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    # Retorna a lista combinada e ordenada.
    return result

def quick_sort(arr):
    """
    Implementa o algoritmo de ordenação Quick Sort.
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas.
    if len(arr) <= 1:
        return arr

    # Escolhemos o pivô como o elemento do meio para evitar os piores casos.
    pivot = arr[len(arr) // 2]

    # Listas para armazenar elementos menores, iguais e maiores que o pivô.
    less_than_pivot = [x for x in arr if x < pivot]  # Elementos menores que o pivô.
    equal_to_pivot = [x for x in arr if x == pivot]  # Elementos iguais ao pivô.
    greater_than_pivot = [x for x in arr if x > pivot]  # Elementos maiores que o pivô.

    # Recursivamente ordenamos as sublistas 'less_than_pivot' e 'greater_than_pivot'.
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
random_array = [random.randint(-100000, 100000) for _ in range(1000)]

start_QS = time.time()
print(quick_sort(random_array))
end_QS = time.time()
total_time_QS = end_QS - start_QS
total_time_QS = str(total_time_QS)

start_MS = time.time()
print(merge_sort(random_array))
end_MS = time.time()
total_time_MS = end_MS - start_MS
total_time_MS = str(total_time_MS)



print("Total time for Merge Sort: " + total_time_MS)
print("total time for Quick Sort: " + total_time_QS)