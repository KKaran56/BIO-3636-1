import random

def split(str):
    return [char for char in str]

target_seq = split('AAAA')
random_seq = split('GCTA')
check = [None] * 4
B = 1000000
count = 0
for i in range(B):
    while check != target_seq:
        for i in range(4):
            if random_seq[i] == target_seq[i]:
                check[i] = random_seq[i]
            else:
                index = random.randint(0, 3)
                check[i] = random_seq[index]
            count += 1
avg = count/B
print(f"Avg: {avg}")
