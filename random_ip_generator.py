import random

def generate_ip_address():
    l = [x for x in range(256)]
    s = []
    s = random.sample(l, 4)
    return '.'.join(str(letter) for letter in s)

print(generate_ip_address())