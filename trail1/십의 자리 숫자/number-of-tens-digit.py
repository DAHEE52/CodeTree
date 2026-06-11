nums = list(map(int, input().split()))
cnt = 0

for i in range(1, 10):
    for j in range(len(nums)):
        if nums[j] == 0:
            break
        else:
            if (nums[j] // 10) == i:
                cnt += 1
        
    print(i, '-', cnt)
    cnt = 0