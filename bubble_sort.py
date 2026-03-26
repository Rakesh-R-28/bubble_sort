print("Bubble Sort")

# Taking input
n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Bubble Sort logic
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            # Swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Output
print("Sorted array:")
for i in range(n):
    print(arr[i], end=" ")