N, Q = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(Q):
    quest = list(map(int, input().split()))

    if quest[0] == 1:
        a = quest[1]
        print(nums[a-1])
    elif quest[0] == 2:
        b = quest[1]
        if b in nums:
            print(nums.index(b)+1)
        else:
            print(0)
    elif quest[0] == 3:
        s = quest[1]
        e = quest[2]
        for i in range(s-1, e):
            print(nums[i], end=' ')
        print()