import numpy as np

str1 = input("длины участков (через пробел): ")
str2 = input("скорости на участках (через пробел): ")
k = int(input("номер участка въезда (k): "))
p = int(input("номер участка выезда (p): "))

lengths = np.array(list(map(float, str1.split())))
speeds = np.array(list(map(float, str2.split())))

n = len(lengths)
if len(speeds) != n:
    raise ValueError("кол-во длин и скоростей должно совпадать.")
if not (1 <= k <= p <= n):
    raise ValueError("должно быть: 1 <= k <= p <= количество участков.")

part_lengths = lengths[k:p]    
part_speeds = speeds[k:p]     

distance = np.sum(part_lengths)
times = part_lengths / part_speeds
total_time = np.sum(times)

average_speed = distance / total_time
print(f"S = {distance:.0f} км, T = {total_time:.2f} час, V = {average_speed:.2f} км/ч")