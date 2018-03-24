import litera as lt

def qsort(arr, l, r):
    if l >= r:
        return
    pivot = arr[l]
    i, j = l, r
    while i <= j:
        while arr[i] > pivot:
            i += 1
        while arr[j] < pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    qsort(arr, l, j)
    qsort(arr, i, r)


def make_code(arr, l, r, codes):
    if r == l + 1:
        codes[l] += "0"
        codes[r] += "1"
        return
    if r <= l:
        return
    a = 0
    b = 0
    for i in range(l, r+1, 1):
        b += arr[i].getprob()
    total = b
    b /= 2
    i = l
    while a <= b:
        a += arr[i].getprob()
        total -= arr[i].getprob()
        i += 1
    if (arr[i-1].getprob() - b) < (a - b):
        i -= 1
    for j in range(l, i, 1):
        codes[j] += "0"
    for j in range(i, r+1, 1):
        codes[j] += "1"
    make_code(arr, l, i-1, codes)
    make_code(arr, i, r, codes)


arr = [lt.Litera('a', 0.3), lt.Litera('b', 0.04), lt.Litera('c', 0.09), lt.Litera('d', 0.14), lt.Litera('e', 0.1),
       lt.Litera('f', 0.05), lt.Litera('g', 0.06), lt.Litera('h', 0.07), lt.Litera('i', 0.01), lt.Litera('j',0.08)]
qsort(arr, 0, 9)
for i in range(10):
    arr[i].printlitera()
codes = ["c" for i in range(len(arr))]
make_code(arr, 0, 9, codes)
print("\n")
for i in range(len(codes)):
    arr[i].printlitera()
    print(" - ", codes[i])
