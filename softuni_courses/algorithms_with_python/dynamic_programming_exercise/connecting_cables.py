nums = [int(x) for x in input().split()]

combinations = [1] * len(nums)

for idx, num in enumerate(nums):
    for idx2 in range(idx - 1, -1, -1):
        if num > nums[idx2]:
            combinations[idx] = max(combinations[idx2] + 1, combinations[idx])

print(f'Maximum pairs connected: {max(combinations)}')
