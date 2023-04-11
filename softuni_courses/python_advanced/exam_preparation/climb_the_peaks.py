from collections import deque

conquered_peaks = []
peaks_difficulty = deque([(80, 'Vihren'),
                          (90, 'Kutelo'),
                          (10, 'Banski Suhodol'),
                          (60, 'Polezhan'),
                          (70, 'Kamenitza')])

daily_portion = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))

for i in range(7):
    current_day = daily_portion.pop() + stamina.popleft()
    if current_day >= peaks_difficulty[0][0]:
        conquered_peaks.append(peaks_difficulty[0][1])
        peaks_difficulty.popleft()

    if len(peaks_difficulty) == 0:
        print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
        break
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if len(conquered_peaks):
    print('Conquered peaks:')
    [print(i) for i in conquered_peaks]
