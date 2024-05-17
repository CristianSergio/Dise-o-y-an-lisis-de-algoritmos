# -*- coding: utf-8 -*-

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def main():
    print("Seleccione el algoritmo de ordenamiento:")
    print("1. Ordenamiento Burbuja")
    print("2. Ordenamiento por Inserción")
    print("3. Ordenamiento por Selección")
    print("4. QuickSort")
    print("5. MergeSort")
    print("6. HeapSort")

    choice = input("Ingrese el número correspondiente a su elección: ")

    arr = list(map(int, input("Ingrese los números a ordenar separados por espacio: ").split()))

    if choice == '1':
        sorted_arr = bubble_sort(arr)
        print("Ordenado por Burbuja:", sorted_arr)
    elif choice == '2':
        sorted_arr = insertion_sort(arr)
        print("Ordenado por Inserción:", sorted_arr)
    elif choice == '3':
        sorted_arr = selection_sort(arr)
        print("Ordenado por Selección:", sorted_arr)
    elif choice == '4':
        sorted_arr = quick_sort(arr)
        print("Ordenado por QuickSort:", sorted_arr)
    elif choice == '5':
        sorted_arr = merge_sort(arr)
        print("Ordenado por MergeSort:", sorted_arr)
    elif choice == '6':
        sorted_arr = heap_sort(arr)
        print("Ordenado por HeapSort:", sorted_arr)
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
