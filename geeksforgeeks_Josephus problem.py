n = 7
k = 3
bin_n = bin(n)[2:]
print(bin_n)

bin_n = bin_n[k:] + bin_n[:k]
print(bin_n)

print(int(bin_n, 2))