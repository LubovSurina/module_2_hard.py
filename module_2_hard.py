n = int(input('Введите число от 3 до 20: '))
print(n)
result = str()
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result += f"{i}{j}"
print(result)