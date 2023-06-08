targets = [int(i) for i in input().split()]
counter = 0
shot_target_idx = []

while True:
    idx = input()

    if idx == 'End':
        print(f"Shot targets: {len(shot_target_idx)} -> {' '.join(map(str, targets))}")
        break

    idx = int(idx)

    if 0 <= idx < len(targets) and idx not in shot_target_idx:
        shot_target_idx.append(idx)
        for i in range(len(targets)):
            if targets[i] > targets[idx] and i not in shot_target_idx:
                targets[i] -= targets[idx]
            elif targets[i] <= targets[idx] and i not in shot_target_idx:
                targets[i] += targets[idx]

        targets[idx] = -1

