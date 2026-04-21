a = [2, 8, 5, 3, 9, 4, 1]
n = len(a)

for j in range(0, n - 1):
    iMin = j
    
    for i in range(j + 1, n):
        if a[i] < a[iMin]:
            iMin = i
            
    if iMin != j:
        # Esto equivale al swap(a[j], a[iMin])
        a[j], a[iMin] = a[iMin], a[j]

print(a)