a = int(input())
for row_num in range(a, 0, -1):
    row_out = ""
    for seq_num in range(1, row_num + 1):
        row_out = row_out + str(seq_num) + " "
    print(row_out)
