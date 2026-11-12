min_pair = 100
max_pair = 0

for i in range(2, 5):
    for j in range(3, 6):
        pair_sum = i * 2 + j
        if pair_sum < min_pair:
            min_pair = pair_sum
        if pair_sum > max_pair:
            max_pair = pair_sum

print("Min:", min_pair)
print("Max:", max_pair)
