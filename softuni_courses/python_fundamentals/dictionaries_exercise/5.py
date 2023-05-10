key_mats = {"shards": 0, "fragments": 0, "motes": 0}
junk_mats = {}
is_found = False
weapons = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
while not is_found:
    x = input().lower().split()
    for i in range(0, len(x), 2):
        if x[i + 1] in key_mats:
            key_mats[x[i + 1]] += int(x[i])
            if key_mats[x[i + 1]] >= 250:
                key_mats[x[i + 1]] -= 250
                print(f"{weapons[x[i + 1]]} obtained!")
                is_found = True
                break
        else:
            if x[i + 1] not in junk_mats:
                junk_mats[x[i + 1]] = 0
            junk_mats[x[i + 1]] += int(x[i])

for mats, values in key_mats.items():
    print(f"{mats}: {values}")
for mats, values in junk_mats.items():
    print(f"{mats}: {values}")
    