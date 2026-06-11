A, B, C, D = 0, 0, 0, 0

for _ in range(3):
    cold, temp = map(str, input().split())
    temp = int(temp)

    if cold == 'Y':
        if temp >= 37:
            A += 1
        else:
            C += 1
    else:
        if temp >= 37:
            B += 1
        else:
            D += 1

if A >= 2:
    print(A, B, C, D, 'E')
else:
    print(A, B, C, D)