n = int(input("Input nilai N:\n"))

# Barisan Genap
print("Barisan genap: ", end="")
for i in range(2, n + 1, 2):
    print(i, end=" ")

print()

# Barisan Ganjil (Lebih efisien tanpa if)
print("Barisan ganjil: ", end="")
for i in range(1, n + 1, 2):
    print(i, end=" ")