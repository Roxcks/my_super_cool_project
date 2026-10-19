import random
import string

bad_chars = set('Il1oO0')

digits = "".join(c for c in string.digits if c not in bad_chars)
upper = "".join(c for c in string.ascii_uppercase if c not in bad_chars)
lower = "".join(c for c in string.ascii_lowercase if c not in bad_chars)
allowed_chars = digits + upper + lower

def generate_password(length):
    password0 = []
    password0.append(random.choice(digits)) 
    password0.append(random.choice(upper)) 
    password0.append(random.choice(lower)) 
    while len(password0) < length:
        password0.append(random.choice(allowed_chars))
    random.shuffle(password0)
    return ''.join(password0)
    
def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n = int(input())
m = int(input())

for password in generate_passwords(n, m):
    print(password)