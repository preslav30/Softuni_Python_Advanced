from collections import deque

daily_portions = list(map(int, input().split(', ')))
daily_stamina = deque(map(int, input().split(', ')))
peaks_count = 0
all_peaks_climbed = False
conquered_peaks = []
peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,
}
i = 1
while i <= 7 and daily_stamina and daily_portions:

    last_food = daily_portions.pop()
    first_stamina = daily_stamina.popleft()
    stamina_plus_food = last_food + first_stamina
    peak = list(peaks)[peaks_count]
    if stamina_plus_food >= peaks[peak]:
        peaks_count += 1
        conquered_peaks.append(peak)
        if peaks_count == 5:
            all_peaks_climbed = True
            print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
            break
    else:
        continue

if not all_peaks_climbed:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print(f'Conquered peaks:')
    print(*conquered_peaks, sep='\n')


