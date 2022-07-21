# 19 July 2022

# Problems:

# Question 1:

# (a) Save p53.txt inside p53_1.txt

file1 = open("p53.txt", "r")
file2 = open("p53_1.txt", "w")
data = file1.readlines()
file2.writelines(data[1:])
file1.close()
file2.close()

# (b) Fine the no of nt. present in p53.txt.

file1 = open("p53_1.txt", "r")
count = len(file1.read())
print(f"Number of nt.: {count}")

# (c) Find out how many ATG & Kozak seq. are there.

def count_atg(seq):
    count = 0
    for i in range(len(seq)):
        if seq[i:i + 3] == 'ATG':
            count += 1
    return count

def count_kozak(seq):
    count = 0
    for i in range(len(seq)):
        slice = seq[i:i + 7]
        if slice[0] == ('A' or 'G') and (slice[3:7] == 'ATGG'):
            count += 1
    return count

file1 = open("p53_1.txt", "r")
seq = file1.read()
print(f"ATG count: {count_atg(seq)}")
print(f"Kozak seq. count: {count_kozak(seq)}")

# Question 2:

# (a) Start with a 4-nt long random DNA seq
# Target seq = "AAAA"
# Copy nt: if the focal nt matches target,
    # 100% fidelity
    # Else, any of hte nt. is copied.
# Find the no. of iterations needed to reach teh target.

import random

def split(str):
    return [char for char in str]

target_seq = split('AAAA')
random_seq = split('GCTA')
check = [None] * 4
B = 100000000
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
    print(f"Done with {i}.")
avg = count/B
print(f"Avg: {avg}")
