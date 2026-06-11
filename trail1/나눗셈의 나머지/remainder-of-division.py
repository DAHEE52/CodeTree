A, B = map(int, input().split())
cnt = [0] * B
total = 0

while A > 1:
    cnt[A % B] += 1
    A = A // B

for n in cnt:
    total += (n ** 2)

print(total)