a = [3, 8, 5, 1, 8, 5, 3, 2, 7]
s = ""
i = 0
while i < len(a):
    if a[i] % 2 != 0:
        number = a[i]
        s += str(a[i]) + str(a[number])
    i += 1

print(s)  # Display the final value of s
