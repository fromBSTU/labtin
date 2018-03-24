import litera as lt


def search_2min(arr):
    min = arr[0]
    min2 = lt.Litera("a", 1)
    min_index = 0
    min2_index = -1
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    for i in range(len(arr)):
        if arr[i] < min2 and i != min_index:
            min2 = arr[i]
            min2_index = i
    return [min_index, min2_index]


def huffmantree(arr):
    while len(arr) > 1:
        min2 = search_2min(arr)
        p = arr[min2[0]].parent(arr[min2[1]])
        del arr[min2[0]]
        if min2[0] > min2[1]:
            del arr[min2[1]]
        else:
            del arr[min2[1] - 1]
        arr.append(p)


def huffmancode(parent):
    parent.union()
    if parent.getlson() is not None:
        huffmancode(parent.getlson())
    if parent.getrson() is not None:
        huffmancode(parent.getrson())


def printtree(parent):
    if parent.getlson() is None and parent.getrson() is None:
        parent.print_with_code()
        print("\n")
    if parent.getlson() is not None:
        printtree(parent.getlson())
    if parent.getrson() is not None:
        printtree(parent.getrson())
