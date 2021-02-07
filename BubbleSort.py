def BubbleSort(sequence):
    length = len(sequence)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, length - 1):
            if sequence[i] > sequence[i + 1]:
                sorted = False
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
        print(sequence)



print(BubbleSort([6, 3, 8, 1, 2, 5, 9]))
