import time
import random


f = open("fisier.in")
g = open("fisier.out", 'w')

v = []
inp = f.readlines()
t = int(inp[0][0])
f.close()

def sorted(l):
    ok = 1
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            ok = 0
    if ok == 0:
        g.write(" NU a fost sortat in")
    else:
        g.write(" a fost sortat in")

def quickSort(v):
    L = []
    E = []
    G = []

    if len(v) <= 1:
        return v
    else:
        pivot = (random.choice(v) + random.choice(v) + random.choice(v)) // 3
        for i in v:
            if i < pivot:
                L.append(i)
            elif i > pivot:
                G.append(i)
            else:
                E.append(i)
        L = quickSort(L)
        G = quickSort(G)
        return L + E + G


def radixsort256(list):
    s = 0
    m = (1 << 8) - 1
    maxim = max(list)
    cc= 0
    while maxim > 0:
        maxim >>= 8
        cc += 1
    for i in range(cc):
        bucket=[[] for j in range(256)]
        for j in list:
            x = (j >> s) & m
            bucket[x].append(j)
        list = []
        for j in range(256):
            list.extend(bucket[j])
        s += 8
    return list

def radixsort(list):
    max_element = max(list)
    place = 1
    while max_element // place > 0:
        countsort(list)
        place *= 10
    return list


def countsort(v):
    m = max(v)
    fr = [0 for i in range(10 ** 6)]
    for x in v:
        fr[x] += 1

    rez = []
    for i in range(10 ** 6):
        while fr[i] > 0:
            rez.append(i)
            fr[i] -= 1

    return rez


def bubblesort(array):
    n = len(array)
    for i in range(n):

         for j in range(0, n - i - 1):

            if array[j] > array[j + 1]:
               array[j], array[j + 1] = array[j + 1], array[j]
    return array


def interclasare(lst, ldr):
    i = j = 0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] < ldr[j]:
            rez.append(lst[i])
            i = i + 1
        else:
            rez.append(ldr[j])
            j = j + 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez


def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mij = len(lista) // 2
        lst = mergesort(lista[:mij])
        ldr = mergesort(lista[mij:])
        return interclasare(lst, ldr)


def genereaza(n, maxim):
    lis = []
    for x in range(n):
        nr = random.randint(0, maxim + 1)
        lis.append(nr)
    return lis


for teste in range(0, t):
    intrare = inp[teste + 1].split()
    n = int(intrare[0])
    maxim = int(intrare[1])
    lista = genereaza(n, maxim)

    g.write('Testul ' + str(teste + 1) + ':\n')
    g.write('valoare maxima este ' + str(maxim) + ' nr. maxim de elemente este ' + str(n) + '\n')
    if maxim < 10 ** 6:
        start_time = time.time()
        sol = countsort(lista)
        g.write('Countsort')
        sorted(sol)
    else:
        start_time = time.time()
        g.write('Countsort ')
        g.write('Nu se poate sorta')
    g.write("  %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    if n <= 3000:
        sol = bubblesort(lista)
        g.write('Bubble Sort')
        sorted(sol)
    else:
        g.write('Bubble Sort ')
        g.write("Nu se poate sorta")
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = radixsort(lista)
    g.write('Radixsort in baza 10')
    sorted(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = radixsort256(lista)
    g.write('Radixsort in baza 256')
    sorted(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = mergesort(lista)
    g.write('Mergesort')
    sorted(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = quickSort(lista)
    g.write('Quicksort')
    sorted(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')
