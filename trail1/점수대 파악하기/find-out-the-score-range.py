scores = list(map(int, input().split()))
cnt = 0

for i in range(10, 0, -1):
    for j in range(len(scores)):
        if scores[j] == 0:
            break
        else:
            if (scores[j] // 10) == i:
                cnt += 1

    print(f"{i}0 - {cnt}")
    cnt = 0