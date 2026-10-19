d = {}
d1 = {}
for _ in range(int(input())):
    number_and_time = input().split(':', 1)
    key = number_and_time[0]
    value = number_and_time[1]
    d.setdefault(key, value)
for _ in range(int(input())):
    time = input().split(':', 1)
    key1 = time[0]
    value1 = time[1]
    d1.setdefault(key1, value1)
for key1 in d1:
    if key1 in d:
        in_parts = d[key].strip().split(':')
        in_total = int(in_parts[0]) * 60 + int(in_parts[1])

        out_parts = d1[key].strip().split(':')
        out_total = int(out_parts[0]) * 60 + int(out_parts[1])

        if in_total > out_total:
            out_total += 24 * 60

        minutes = out_total - in_total
        if minutes > 120:
            cost = (minutes - 120) * 3
            print(f"{key1}: {cost}₽")
        else:
            print(f'{key}: плата не взимается')




    
