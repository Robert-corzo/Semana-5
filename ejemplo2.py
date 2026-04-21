a = [2, 8, 5, 3, 9, 4, 1]
N = len(a)


for i in range(1, N + 1):
    for j in range(0, N - 1):
        if a[j] > a[j + 1]:
            # swap(a[j], a[j + 1])
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)