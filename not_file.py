d = {}
d1 = {}

word = input()
num = int(input())
for _ in range(num):
    letter_frequency = input().split(': ')
    key = letter_frequency[0]
    value = int(letter_frequency[1])
    d[key] = d.get(key, 0) + value
inverted_d = {value: key for key, value in d.items()}
for letter in word:
    d1[letter] = d1.get(letter, 0) + 1
inverted_d1 = {value1: key1 for key1, value1 in d1.items()}
decoded_word = ""
for letter in word:
    freq = d1[letter]          
    real_letter = inverted_d[freq]  
    decoded_word += real_letter

print(decoded_word)
    
    
    




