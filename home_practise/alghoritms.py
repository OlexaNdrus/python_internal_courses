def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(array):
    for i in range(len(array)):
        lowest_el = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest_el]:
                lowest_el = j
            array[i], array[lowest_el] = array[lowest_el], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        unsorted_value_ind = i - 1
        while unsorted_value_ind>=0 and array[unsorted_value_ind]>item_to_insert:
            unsorted_value_ind -= 1
        array.insert(unsorted_value_ind+1, item_to_insert)
        del array[i+1]


test_arr = [1, 4, 6, 7, 2, 11, 0]
#selection_sort(test_arr)
#print(test_arr)

insertion_sort(test_arr)
print(test_arr)

def partition(nums, low, high):
    # Мы выбираем средний элемент, в качестве опорного. Некоторые реализации выбирают
    # первый элемент или последний элемент или вообще случайный элемент.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Если элемент в i (слева от оси) больше, чем
        # элемент в J (справа от оси), то поменять их местами
        nums[i], nums[j] = nums[j], nums[i]
def quick_sort(nums):
    # Создаем вспомогательную рекурсивную функцию
    def _quick_sort(items, low, high):
        if low < high:
            # Это индекс после опорного элемента, по которому наши списки разделены
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)
# Проверяем, что все работает
random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)