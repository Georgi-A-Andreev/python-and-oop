from collections import deque

cards = deque(input().split())
shuffles = int(input())

left_side = []
right_side = []

shuffled_deck = []

for i in range(len(cards) // 2):
    left_side.append(cards.popleft())
    right_side = cards.copy()

for i in range(shuffles):
    shuffled_deck.clear()
    for j in range(len(left_side)):

        shuffled_deck.append(left_side[j])
        shuffled_deck.append(right_side[j])

    left_side = shuffled_deck[:len(shuffled_deck) // 2]
    right_side = shuffled_deck[len(shuffled_deck) // 2:]

print(shuffled_deck)
