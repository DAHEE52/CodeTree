N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

for n in nums:
    if n == M:
        cnt += 1

print(cnt)